import express, { json } from 'express';
import { createClient } from 'redis';
import { createQueue } from 'kue';
import { promisify } from 'util';

const app = express();
const client = createClient();
const queue = createQueue();

// Promisify Redis methods
const hgetAsync = promisify(client.hget).bind(client);
const hsetAsync = promisify(client.hset).bind(client);

// Function to reserve seat
async function reserveSeat(number) {
  await hsetAsync('available_seats', 'numberOfAvailableSeats', number);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
  const seats = await hgetAsync('available_seats', 'numberOfAvailableSeats');
  return parseInt(seats) || 0;
}

// Initialize available seats to 50
reserveSeat(50);

// Initialize reservationEnabled
let reservationEnabled = true;

// Middleware to parse JSON
app.use(json());

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Route to reserve seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      return res.json({ status: 'Reservation in process' });
    } else {
      return res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

// Route to process queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Decrease available seats and check if reservation is still enabled
  const availableSeats = await getCurrentAvailableSeats();
  if (availableSeats === 0) {
    reservationEnabled = false;
  } else if (availableSeats < 0) {
    throw new Error('Not enough seats available');
  }

  queue.process('reserve_seat', async (job, done) => {
    await reserveSeat(availableSeats - 1);
    done();
  });
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

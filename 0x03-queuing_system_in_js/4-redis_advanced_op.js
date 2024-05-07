import redis from 'redis'

// Create a Redis client
const client = redis.createClient();

// On connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// On error event
client.on('error', error => {
    console.error(`Redis client not connected to the server: ${error}`);
});

// Create Hash
client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

// Display Hash
client.hgetall('HolbertonSchools', (err, reply) => {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log(reply);
  }
});


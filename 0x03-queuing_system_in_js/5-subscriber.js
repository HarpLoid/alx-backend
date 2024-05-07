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

client.subscribe('holberton school channel');

client.on('message', message => {
    console.log(message);
    if(message === 'KILL_SERVER') {
        client.unsubscribe();
        client.quit();
    }
})

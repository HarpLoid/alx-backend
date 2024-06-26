import redis from "redis";

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client conected to the server');
});

client.on('error', error => {
    console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.error('Error', err);
        } else {
            console.log(reply);
        }
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

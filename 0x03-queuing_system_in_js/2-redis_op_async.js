import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client conected to the server');
});

client.on('error', error => {
    console.error(`Redis client not connected to the server: ${error}`);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
    const reply = await setAsync(schoolName, value);
    console.log('Reply:', reply);
}

async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error('Error', error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

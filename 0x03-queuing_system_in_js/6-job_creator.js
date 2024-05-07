import { createQueue } from "kue";

const queue = createQueue();

const job = {
    phoneNumber: '55503454',
    message: 'Hello Guys',
}

const jobQueue = queue.create('push_notification_code', job);

jobQueue.on('enqueue', () => {
    console.log('Notification job created:', jobQueue.id);
});

jobQueue.on('complete', () => {
    console.log('Notification job completed');
});

jobQueue.on('failed', () => {
    console.log('Notification job failed');
});

jobQueue.save();
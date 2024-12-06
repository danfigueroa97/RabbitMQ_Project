const amqp = require('amqplib/callback_api');

// Conectar al broker
amqp.connect('amqp://localhost', (err, conn) => {
    if (err) {
        console.error(err);
        return;
    }

    conn.createChannel((err, channel) => {
        if (err) {
            console.error(err);
            return;
        }

        const queue = 'queue1';

        // Declarar la cola
        channel.assertQueue(queue, { durable: false });

        console.log(`Subscriber 1 esperando mensajes en ${queue}`);

        // Recibir mensajes
        channel.consume(queue, (msg) => {
            console.log(`Subscriber 1 recibió: ${msg.content.toString()}`);
        }, { noAck: true });
    });
});

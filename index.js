const qrcode = require('qrcode-terminal');
const { MessageMedia } = require('whatsapp-web.js');

//Crea una sesión con whatsapp-web y la guarda localmente para autenticarse solo una vez por QR
const { Client, LocalAuth } = require('whatsapp-web.js');
const client = new Client({
    authStrategy: new LocalAuth(),
});

//Genera el código qr para conectarse a whatsapp-web
client.on('qr', qr => {
    qrcode.generate(qr, { small: true });
});

// Number where you want to send the message.
const numbers = ['5529282277', '5529282277', '5529282277', '5529282277', '5529282277'];

// Your media
const media = MessageMedia.fromFilePath('./img.jpg');

// Your message.
const text = `¡Hola :) !  ¡Disfruta de la nueva colección en *Elements Joyería!* \nRealiza fácilmente tu pedido en : elements-of-steel.com.mx/catalog/ * O con tu vendedor de confianza :)
        \n*Recuerda *ingresar tu número celular como usuario y contraseña*
        \nSi prefieres catálogo en PDF avísame ;D`;

setTimeout(() => {
    numbers.forEach(number => {
        client.on('ready', () => {

            const chatId = '521' + number + '@c.us';

            // Sending message.
            client.isRegisteredUser(chatId).then(async function (isRegistered) {
                if (isRegistered) {
                    await client.sendMessage(chatId, media);
                    await client.sendMessage(chatId, text);
                    console.log('Enviado: ' + chatId);
                } else {
                    console.log(chatId + ' No Registrado');
                }
            })
        });
    });

    client.initialize();

}, 15000)


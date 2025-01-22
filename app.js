const mineflayer = require('mineflayer');

// Create the bot
const bot = mineflayer.createBot({
  host: '209.25.141.121', // Minecraft server IP
  port: 25565,       // Minecraft server port
  username: 'BotName' // Minecraft username
});

// Listen for chat messages in the game
bot.on('chat', (username, message) => {
  if (username === bot.username) return; // Ignore bot's own messages
  bot.chat(`Hello, ${username}! You said: ${message}`);
});

// Listen for terminal input
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', (input) => {
  if (input === '#stop') {
    // Special command to stop the bot
    bot.chat('Goodbye! Stopping the bot...');
    rl.close();
    bot.end();
    console.log('Bot stopped.');
    process.exit(0); // Exit the program
  } else {
    // Send any other input as a command or chat message
    bot.chat(input);
  }
});

// Event listeners for debugging and stability
bot.on('spawn', () => console.log('Bot has spawned into the world!'));
bot.on('error', (err) => console.error('Error:', err));
bot.on('kicked', (reason) => console.log('Kicked for:', reason));

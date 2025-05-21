const mineflayer = require('mineflayer')
const Vec3 = require('vec3')

const bot = mineflayer.createBot({
host: 'localhost',   // Change to your server IP or 'localhost' for singleplayer
port: 25565,         // Change to your server port
username: 'ParkourBot'
})

// Add error handling
bot.on('error', (err) => {
console.error('Bot encountered an error:', err)
})

bot.on('spawn', () => {
console.log('Bot spawned and ready')
bot.chat('/tp ParkourBot -336 8 -148')
console.log('Teleport command sent, waiting 2 seconds...')

setTimeout(() => {
    console.log('Timeout completed, attempting to look...')
    // Look toward yaw 0 (south), pitch 0
    const yaw = 0
    const pitch = 0
    
    // Add a safety timeout in case the look callback never fires
    const lookTimeout = setTimeout(() => {
    console.log('WARNING: Look callback did not execute within 5 seconds')
    continueWithExecution(bot.entity.position, yaw)
    }, 5000)
    
    try {
    bot.look(yaw, pitch, true, () => {
        clearTimeout(lookTimeout) // Clear the safety timeout
        console.log('Look completed, getting position and blocks...')
        continueWithExecution(bot.entity.position, yaw)
    })
    } catch (err) {
    console.error('Error during look operation:', err)
    clearTimeout(lookTimeout)
    continueWithExecution(bot.entity.position, yaw)
    }
    
    // Move the execution into a separate function to avoid duplication
    function continueWithExecution(pos, yaw) {
    console.log('Bot position:', pos)
    // Calculate forward vector for yaw 0
    const forwardVec = {
        x: -Math.sin(yaw),
        y: 0,
        z: Math.cos(yaw)
    }
    // Center of the 3x3x3 cube is 1 block in front of the bot
    const center = {
        x: pos.x + forwardVec.x,
        y: pos.y,
        z: pos.z + forwardVec.z
    }
    
    console.log('Center position for block detection:', center)
    
    try {
        console.log('--- Blocks in front of bot (printed to terminal) ---')
        for (let dy = 1; dy >= -1; dy--) { // y: top to bottom
        console.log(`Layer y+${dy}:`)
        for (let dz = -1; dz <= 1; dz++) {
            let row = ''
            for (let dx = -1; dx <= 1; dx++) {
            const x = Math.floor(center.x + dx)
            const y = Math.floor(center.y + dy)
            const z = Math.floor(center.z + dz)
            const block = bot.blockAt(new Vec3(x, y, z))
            row += (block ? block.name : 'air').padEnd(12)
            }
            console.log(row)
        }
        console.log('')
        }
        console.log('--- End of block printout ---')
        
        // Move forward after rotating and printing blocks
        setTimeout(() => {
        bot.setControlState('forward', true)
        setTimeout(() => bot.setControlState('forward', false), 3000)
        }, 1000)

        // Make the bot jump every 2 seconds
        setInterval(() => {
        bot.setControlState('jump', true)
        setTimeout(() => bot.setControlState('jump', false), 200)
        }, 2000)
    } catch (err) {
        console.error('Error while processing blocks:', err)
    }
    }
}, 2000) // Wait 2s for teleport to complete
})

// Add login handler to confirm connection
bot.on('login', () => {
console.log('Bot successfully logged in')
})

// Add physicsTick handler to check if bot is active
bot.on('physicsTick', () => {
if (!bot.physicsTick_logged) {
    console.log('Physics engine active')
    bot.physicsTick_logged = true
}
})

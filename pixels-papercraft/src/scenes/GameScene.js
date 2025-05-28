import Phaser from 'phaser'; // Keep this import for ES Module consistency

export default class GameScene extends Phaser.Scene {
    constructor() {
        super('GameScene');
        this.player = null; // Initialize player
        this.cursors = null; // Initialize cursors
        this.ground = null; // Initialize ground
    }

    preload() {
        // All assets are preloaded in PreloadScene.js, so this method can be empty.
        // Do NOT load assets here again.
    }

    create() {
        console.log('GameScene created.');

        // Add graph paper background
        // Set origin to top-left (0,0) for easier positioning if background is full screen
        this.add.image(0, 0, 'graph_paper_background').setOrigin(0, 0);

        // Create ground platform
        this.ground = this.physics.add.staticGroup();
        this.ground.create(512, 580, 'pixel_paradox_placeholder') // Using placeholder as a temporary texture
            .setScale(32, 1) // Make it wide and flat
            .refreshBody(); // Update physics body after scaling
        this.ground.setAlpha(0.5); // Make it semi-transparent for now, for visibility during development

        // Create player
        this.player = this.physics.add.sprite(100, 450, 'pixel_paradox_placeholder');
        this.player.setBounce(0.2); // Add a slight bounce
        this.player.setCollideWorldBounds(true); // Keep player within camera bounds

        // Add A1 hologram (static for now)
        this.add.image(900, 100, 'a1_hologram_placeholder');

        // Add collision between player and ground
        this.physics.add.collider(this.player, this.ground);

        // Input Cursors
        this.cursors = this.input.keyboard.createCursorKeys();

        // Play background music (e.g., the start screen music)
        // Ensure 'stuck_between_pages' was loaded in PreloadScene
        this.sound.play('stuck_between_pages', { loop: true, volume: 0.5 });

        // Set camera to follow the player
        // Set camera bounds to the game world size
        this.cameras.main.setBounds(0, 0, this.game.config.width, this.game.config.height);
        // Start following the player with a slight lerp (smoothness)
        this.cameras.main.startFollow(this.player, true, 0.05, 0.05);
    }

    update() {
        // Player movement logic
        const playerSpeed = 200; // Increased speed for tighter feel
        const jumpVelocity = -450; // Increased jump velocity

        if (this.cursors.left.isDown) {
            this.player.setVelocityX(-playerSpeed);
            // Future: Add player.anims.play('left', true);
        } else if (this.cursors.right.isDown) {
            this.player.setVelocityX(playerSpeed);
            // Future: Add player.anims.play('right', true);
        } else {
            this.player.setVelocityX(0);
            // Future: Add player.anims.play('turn');
        }

        // Player jump logic
        // Check if 'up' arrow is down AND player is touching the ground
        if (this.cursors.up.isDown && this.player.body.touching.down) {
            this.player.setVelocityY(jumpVelocity);
        }
    }
}

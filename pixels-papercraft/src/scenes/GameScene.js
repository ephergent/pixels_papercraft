import Phaser from 'phaser';

export default class GameScene extends Phaser.Scene {
    constructor() {
        super('GameScene');
    }

    preload() {
        // Load assets
        this.load.image('pixel_paradox_placeholder', 'pixels-papercraft/assets/art/pixel_paradox_placeholder.png');
        this.load.image('a1_hologram_placeholder', 'pixels-papercraft/assets/art/a1_hologram_placeholder.png');
        this.load.image('graph_paper_background', 'pixels-papercraft/assets/art/graph_paper_background.png');
    }

    create() {
        // Add background
        this.add.image(512, 300, 'graph_paper_background');

        // Create ground
        this.ground = this.physics.add.staticGroup();
        this.ground.create(512, 580, 'pixel_paradox_placeholder')
            .setScale(32, 1)
            .refreshBody();
        this.ground.setAlpha(0.5); // Make it semi-transparent for now, for visibility during development

        // Create player
        this.player = this.physics.add.sprite(100, 450, 'pixel_paradox_placeholder');
        this.player.setCollideWorldBounds(true);
        this.physics.add.collider(this.player, this.ground);

        // Input Cursors
        this.cursors = this.input.keyboard.createCursorKeys();
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
        if (this.cursors.up.isDown && this.player.body.touching.down) {
            this.player.setVelocityY(jumpVelocity);
        }
    }
}

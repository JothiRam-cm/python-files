document.addEventListener("DOMContentLoaded", function () {
    const canvas = document.createElement("canvas");
    const context = canvas.getContext("2d");
    document.body.appendChild(canvas);

    canvas.width = 1040;
    canvas.height = 1600;

    const spaceshipImage = new Image();
    spaceshipImage.src = "/image/ship.gif";

    const bulletImage = new Image();
    bulletImage.src = "/image/bullet.gif";

    const enemyImage = new Image();
    enemyImage.src = "/image/enemy.gif";

    const explosionImage = new Image();
    explosionImage.src = "/image/explosion.gif";

    const laserSound = new Audio("/audio/laser.wav");
    const explosionSound = new Audio("/audio/explosion.wav");

    const spaceship = {
        x: canvas.width / 2,
        y: canvas.height - 200,
        width: 50,
        height: 50,
        speed: 3,
    };

    const bullet = {
        x: 0,
        y: 0,
        width: 10,
        height: 30,
        speed: 5,
        visible: false,
    };

    let enemies = [];
    const enemySpeed = 3;

    let score = 0;
    let explosionTimers = [];

    function createEnemy() {
        const enemy = {
            x: Math.random() * (canvas.width - 50),
            y: -50,
            width: 50,
            height: 50,
            visible: true,
        };
        enemies.push(enemy);
    }

    function draw() {
        context.clearRect(0, 0, canvas.width, canvas.height);

        context.drawImage(spaceshipImage, spaceship.x, spaceship.y, spaceship.width, spaceship.height);

        if (bullet.visible) {
            context.drawImage(bulletImage, bullet.x, bullet.y, bullet.width, bullet.height);
        }

        enemies.forEach((enemy, index) => {
            if (enemy.visible) {
                context.drawImage(enemyImage, enemy.x, enemy.y, enemy.width, enemy.height);
            }
        });

        explosionTimers.forEach((timer, index) => {
            if (timer > 0) {
                context.drawImage(explosionImage, enemies[index].x, enemies[index].y, enemies[index].width, enemies[index].height);
            }
        });

        context.fillStyle = "gold";
        context.font = "25px Arial";
        context.textAlign = "right";
        context.fillText(`Score: ${score}`, canvas.width - 20, 30);
    }

    function update() {
        if (bullet.visible) {
            bullet.y -= bullet.speed;
            if (bullet.y < 0) {
                bullet.visible = false;
            }
        }

        if (spaceship.x < 0) {
            spaceship.x = 0;
        } else if (spaceship.x > canvas.width - spaceship.width) {
            spaceship.x = canvas.width - spaceship.width;
        }

        enemies.forEach((enemy, index) => {
            if (enemy.visible) {
                enemy.y += enemySpeed;

                if (bullet.visible &&
                    bullet.x < enemy.x + enemy.width &&
                    bullet.x + bullet.width > enemy.x &&
                    bullet.y < enemy.y + enemy.height &&
                    bullet.y + bullet.height > enemy.y) {

                    explosionTimers[index] = 1;
                    bullet.visible = false;
                    explosionSound.play();
                    score += 100;
                }

                if (explosionTimers[index] > 0) {
                    explosionTimers[index]++;
                }

                if (explosionTimers[index] > 5) {
                    enemy.visible = false;
                }

                if (enemy.y > canvas.height) {
                    enemy.visible = false;
                }
            }
        });

        enemies = enemies.filter(enemy => enemy.visible);

        draw();
        requestAnimationFrame(update);
    }

    document.addEventListener("keydown", function (event) {
        if (event.key === "ArrowLeft") {
            spaceship.x -= spaceship.speed;
        } else if (event.key === "ArrowRight") {
            spaceship.x += spaceship.speed;
        } else if (event.key === " ") {
            if (!bullet.visible) {
                bullet.x = spaceship.x + spaceship.width / 2 - bullet.width / 2;
                bullet.y = spaceship.y - bullet.height;
                bullet.visible = true;
                laserSound.play();
            }
        }
    });

    setInterval(createEnemy, 1000);

    spaceshipImage.onload = function () {
        update();
    };
});

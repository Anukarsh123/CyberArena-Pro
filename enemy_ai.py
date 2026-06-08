class EnemyAI:

    def follow_player(self, enemy, player):

        if enemy.x > player.x:

            enemy.x -= 1

        elif enemy.x < player.x:

            enemy.x += 1

        if enemy.y > player.y:

            enemy.y -= 1

        elif enemy.y < player.y:

            enemy.y += 1

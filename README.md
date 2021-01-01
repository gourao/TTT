# TTT

Designed to teach AI to python programmers.  This has an outline of the minimax skeleton to be filled in and completed by the student.


The following techniques shown below are indicative of a way to "never lose", not necessarily to win. The worst scenario, however, would be to tie.

Remember that there are two basis starting points from which we can plot our strategy - You go first, or your opponent goes first.

But let's review some basic definitions here.






Counter-Attack - Making a move that blocks your opponent
Center - The square in the middle surrounded by all the other squares.
Edge - A piece bordering the center.
Corner - A piece bordered by two edge squares.

Ok - Good! We've got some basic vocabulary down. Now let's get going.



IF YOU GO FIRST...

Avoid placing your first piece on an edge square, and keep it on the center or a corner square. Placing it on an edge square will leave you vulnerable and give your opponent the advantage.

1) Center

If you mark the center, your opponent will either place his/her first piece on an edge or corner piece.


If they mark an edge, it's incredibly easy to win - There's no chance of even tying. Simply place your next piece on one of the two corners furthest from the edge piece. They will most likely block that move, which in turn gives them an opportunity to win. Block their move, and suddenly, you have two ways to win, and your opponent is helpless.

![img](https://qph.fs.quoracdn.net/main-qimg-909c4cd5791ce72dbb60e59c55fc0497.webp)

If they mark a corner, as a smarter opponent would, it's a little bit more complicated. Place your next mark on the opposite corner, or the corner that would make a diagonal of two X's and one O. If they place their next piece on an edge, they've made a mistake, and you now have two ways of winning, depending on which edge they placed their O on. Otherwise, assuming you keep counter-attacking, the game will end in a tie.


![img](https://qph.fs.quoracdn.net/main-qimg-48c9c5073adbb6825e09dfc3515d4790.webp)

2) Corner

If you play a corner piece first, there are only two significant response that your opponent can make: Center, or not center.


If their first move is away from the center, you should be able to win. Remember that your first piece is contained in both a vertical and horizontal row. Your next move should be in the other corner of the same row you placed your first piece. They'll likely counter-attack, leaving two options for you, and an easy path to victory. This will work whether they play a corner or an edge piece first up.


![img](https://qph.fs.quoracdn.net/main-qimg-6e2dc2e1f7e0f4faae9f7b2c1adae54e.webp)

Here's another great way to trap your opponent:

![img](https://qph.fs.quoracdn.net/main-qimg-4fd02cf4e39db99faaf000e13d5c75f4.webp)



If their first move is in the center, it's a little bit trickier. Again, form a diagonal. If their next move is in the corner, you can trap them by placing your next piece at the intersection of the row and column of the previous two X's. If their next move is at an edge, you'll be forced to settle for a draw.


![img](https://qph.fs.quoracdn.net/main-qimg-a3f2d4ff6330fef53ea986775c2b355c.webp)

IF YOUR OPPONENT GOES FIRST...

Unfortunately, if your opponent goes first and uses all the above techniques, there's no way that you can win. In fact, the only way you can win is if his/her first move is an edge piece. If so, carry out all the steps shown above.

So what can you do to at least bring the match to a draw, given that your opponent plays a good strategy?

Remember what we said before - Your opponent will either choose a corner or the center piece.

1) Center

If he chooses the center, place your O on the corner immediately, which will buy you some time. According to the best strategy, your opponent will place his next X on the opposite corner to yours. Your next piece should not be bordering your previous move. Then, it's the simple matter of continuously blocking and counter-attacking until a tie is reached.


![img](https://qph.fs.quoracdn.net/main-qimg-ebdfbaad3d3c4fb8acf0843346097dbf.webp)

Even if they don't use this strategy, keep blocking until you reach a tie.

2) Corner

If they mark a corner, mark the center, or you will almost certainly lose against a good opponent. Then remember that there is one outcome in which a tie is possible from above.

Your opponent has two choices, to either form a diagonal or place their next piece somewhere else. Assuming that their move forms a diagonal, as the strategy would dictate, stay on the edges and off the corners. You can force a tie this way.

![img](https://qph.fs.quoracdn.net/main-qimg-7053455ee1e432172bbcc0cd34d44502.webp)

Else, as usual, keep blocking until a tie is reached.

Of course, this is the logic of Tic-Tac-Toe, but there are certain useful tips that can help you when playing with a good player.


Don't be a reactionary, impulsive player. Unless there's a time limit, take as much time as you want, thinking the move through. Don't react immediately to what your opponent is doing; Sometimes the most obvious move might not be the right one.
Make safe moves. Every move of yours should be dictated by strategy - In the middle of the game, the best way to make a move is to think a few moves ahead, and what your opponent might do. First consider whether a certain move can win you the game, or block the opponent from winning. If not, then make sure to always think strategy. The best way to win is to figure out how to create two ways to win at once.

#include "Game.h"

int main() {
    //init srand
    std::srand(static_cast<unsigned>(time(NULL)));

    //init Game engine
    Game game;

    //Game Loop
    while(game.running() && !game.getEndGame()) {

        //Update
        game.update();
        //Render
        game.render();
        //Draw your game

    }

    //End of application
    return 0;
}

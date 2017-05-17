//
// Created by ziv on 05/05/17.
//

#ifndef TRYSCREEN_ICONDISPLAY_H
#define TRYSCREEN_ICONDISPLAY_H

#include <U8g2lib.h>

struct IconViewModel {
    IconViewModel(bool play, bool shuffle, bool repeat) {
        this->play = play;
        this->shuffle = shuffle;
        this->repeat = repeat;
    }
    IconViewModel(){
        play = false;
        shuffle = false;
        repeat = false;
    }
    const void PrintDebug() const{
        Serial.print("play=");
        Serial.print(play);
        Serial.print(" shuffle=");
        Serial.print(shuffle);
        Serial.print(" repeat=");
        Serial.println(repeat);
    }

    bool play;
    bool shuffle;
    bool repeat;
};

class IconDisplay {
public:
    IconDisplay(U8G2 *);

    void UpdateStatus(const IconViewModel&);

    void Draw();

private:
    U8G2 *screen;
    IconViewModel current;
};


#endif //TRYSCREEN_ICONDISPLAY_H

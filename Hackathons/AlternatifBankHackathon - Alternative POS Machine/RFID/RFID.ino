#include <MFRC522.h>
#include <SPI.h>
#include <ros.h>
#include <std_msgs/Int32.h>

int RST_PIN=9;
int SS_PIN=10;
const int buzzer = x;

MFRC522 rfid(SS_PIN, RST_PIN);
byte ID[4] = {0,0,0,0};

ros::NodeHandle nh;

std_msgs::Int32 msg;
ros::Publisher cardID("cardID", &msg);

void setup() {

  SPI.begin();
  rfid.PCD_Init();
  pinMode(buzzer, OUTPUT);

  nh.initNode();
  nh.advertise(cardID);

}

void loop() {

  if(! rfid.PICC_IsNewCardPresent()){
    return;
    }

  if(! rfid.PICC_ReadCardSerial()){
    return;
    }

  if( rfid.uid.uidByte[0] == ID[0] && 
  rfid.uid.uidByte[1] == ID[1] && 
  rfid.uid.uidByte[2] == ID[2] && 
  rfid.uid.uidByte[3] == ID[3]){
    msg.data = 1;
    cardID.publish(&std_msg);
    delay(1000);
  }

  else{
    msg.data = 0;
    cardID.publish(&std_msg);
    delay(1000);
  }

  nh.spinOnce();
}

//********************************************
//* Robotic Arm with USB control
//* for robotic arm 0
//* By Group 5
//* Aug 15 2018
//********************************************
#include <CurieBLE.h>
#include <Servo.h>
#include <string.h>  
#define ROBOT_NAME "Group2"
#define CRAW_MIN 0 //open
#define CRAW_MAX 58 //close
#define ELBOW_MIN   0
#define ELBOW_MAX 140
#define SHOULDER_MIN 0
#define SHOULDER_MAX 165
#define WRIST_X_MIN 0
#define WRIST_X_MAX 180
#define WRIST_Y_MIN 0
#define WRIST_Y_MAX 90
#define WRIST_Z_MIN 0
#define WRIST_Z_MAX 180
#define BASE_MIN 0
#define BASE_MAX 180
#define ELBOW_DEFAULT 110
#define SHOULDER_DEFAULT 68
#define WRIST_X_DEFAULT 87
#define WRIST_Y_DEFAULT 70
#define WRIST_Z_DEFAULT 65
#define BASE_DEFAULT 96
#define CRAW_DEFAULT 30 //fully opened
#define GRAB_SPEED 500
Servo myservoA;
Servo myservoB;
Servo myservoC;
Servo myservoD;
Servo myservoE;
Servo myservoF;
Servo myservoG;//the craw
int i,pos,myspeed;
int sea,seb,sec,sed,see,sef,seg;

void movement(Servo device, int movespeed, int des){
  for(pos=0;pos<=movespeed;pos+=1)
   {
    device.write(int(map(pos,1,movespeed,device.read(),des)));
    delay(1);
   }
}





void myservosetup()  //set up the servo motors
{
   sea=myservoA.read();
   seb=myservoB.read();
   sec=myservoC.read();
   sed=myservoD.read();
   see=myservoE.read();
   sef=myservoF.read();
   seg=myservoG.read();

   myspeed=500;
   for(pos=0;pos<=myspeed;pos+=1)
   {
    myservoA.write(int(map(pos,1,myspeed,sea,ELBOW_DEFAULT)));
    myservoB.write(int(map(pos,1,myspeed,seb,SHOULDER_DEFAULT)));
    myservoC.write(int(map(pos,1,myspeed,sec,WRIST_X_DEFAULT)));
    myservoD.write(int(map(pos,1,myspeed,sed,WRIST_Y_DEFAULT)));
    myservoE.write(int(map(pos,1,myspeed,see,WRIST_Z_DEFAULT)));
    myservoF.write(int(map(pos,1,myspeed,sef,BASE_DEFAULT)));
    myservoG.write(int(map(pos,1,myspeed,seg,CRAW_DEFAULT)));
    delay(1);
   }
   delay(5);
}

void grab(){
  movement(myservoA, GRAB_SPEED, 76);
  movement(myservoB, GRAB_SPEED, 76);
  movement(myservoE, GRAB_SPEED, 96);
  movement(myservoG, GRAB_SPEED, 0);
  movement(myservoA, GRAB_SPEED, 56);
  movement(myservoB, GRAB_SPEED, 85);
  movement(myservoE, GRAB_SPEED, 105);
  movement(myservoA, GRAB_SPEED, 34);
  movement(myservoB, GRAB_SPEED, 73);
  movement(myservoA, GRAB_SPEED, 21);
  movement(myservoB, GRAB_SPEED, 68);
  movement(myservoE, GRAB_SPEED, 90);
  movement(myservoB, GRAB_SPEED, 63);
  movement(myservoG, GRAB_SPEED, 100);
  movement(myservoA, GRAB_SPEED*3, 60);
  movement(myservoB, GRAB_SPEED*3, 25);
  movement(myservoA, GRAB_SPEED*5, 100);
  //back
  movement(myservoF, GRAB_SPEED*7, 96);
  movement(myservoB, GRAB_SPEED * 5, 60);
  movement(myservoA, GRAB_SPEED * 5, 60);
  movement(myservoE, GRAB_SPEED * 3, 110);
  movement(myservoG, GRAB_SPEED, 30);
  myservosetup();
}

void movements(int elbow_pos)
{
   sea=myservoA.read();


   for(pos=0;pos<=myspeed;pos+=1)
   {
    myservoA.write(int(map(pos,1,myspeed,sea,elbow_pos)));
    delay(1);
   }
}

void setup()
{
  Serial.begin(9600);
  //pinMode(13, OUTPUT);   LED control

  myservoA.attach(2);
  myservoB.attach(3);
  myservoC.attach(4);
  myservoD.attach(5);
  myservoE.attach(6);
  myservoF.attach(8);
  myservoG.attach(7);

  myservosetup();

}

void loop()
{
  	String readString = "";
  	while(!Serial.available()){}
 	while(Serial.available()){
 		if (Serial.available() >0){
      		char c = Serial.read();  //gets one byte from serial buffer
      		readString += c; //makes the string readString
    	}
 	}

 	if (readString.length() >0){
    	Serial.print("Arduino received: ");
		Serial.println(readString); //see what was received
  	}

 	String devNo = readString.substring(0,1);
 	String devAngle = readString.substring(2,readString.length());

 	int devno = devNo.toInt();
 	int devangle = devAngle.toInt();

   sea=myservoA.read();
   seb=myservoB.read();
   sec=myservoC.read();
   sed=myservoD.read();
   see=myservoE.read();
   sef=myservoF.read();
   seg=myservoG.read();

 	switch(devno){
    case 0:
      grab();
      break;
 		case 1:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoA.write(int(map(pos,1,myspeed,sea,devangle)));   
    			delay(1);
   			}
   			break;
 		case 2:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoB.write(int(map(pos,1,myspeed,seb,devangle)));   
    			delay(1);
   			}
   			break;
 		case 3:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoC.write(int(map(pos,1,myspeed,sec,devangle)));   
    			delay(1);
   			}
   			break;
		case 4:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoD.write(int(map(pos,1,myspeed,sed,devangle)));   
    			delay(1);
   			}
   			break;
 		case 5:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoE.write(int(map(pos,1,myspeed,see,devangle)));   
    			delay(1);
   			}
   			break;
 		case 6:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoF.write(int(map(pos,1,myspeed,sef,devangle)));   
    			delay(1);
   			}
   			break;
 		case 7:
 			for(pos=0;pos<=myspeed;pos+=1){
    			myservoG.write(int(map(pos,1,myspeed,seg,devangle)));   
    			delay(1);
   			}
   			break;
 	}

}


/*  *******************SNAKE GAME (BY KULDEEP KUMAR)*******************

    *******************************************************************/

//  HEADER FILES USED

  #include<stdio.h>
  #include<conio.h>
  #include<graphics.h>
  #include<dos.h>
  #include<time.h>


//  FUNCTIONS USED

  void layout();
  void begin();
  void controls();
  void score();
  void closing();

  void main()
 {
   int gd=DETECT,gm,x,y;
   initgraph(&gd,&gm,"c:\\TC\\bgi");

   layout();
   begin();
   controls();
   score();
   closing();

   getch();
   closegraph();
   restorecrtmode();
  }

  void layout()
  { int i;char ch;
    setbkcolor(BLACK);
    for(i=10;i<=500;i++)
      { bar3d(i,10,i,10,5,1);
	setcolor(WHITE);
      }
       for(i=10;i<=400;i++)
      { bar3d(500,i,500,i,5,1);
	setfillstyle(2,WHITE);
      }
       for(i=500;i>=10;i--)
      { bar3d(i,400,i,400,5,1);
	setcolor(WHITE);
      }
       for(i=10;i<=400;i++)
      { bar3d(10,i,10,i,5,1);
	setfillstyle(2,WHITE);
      }
      setcolor(GREEN);
      settextstyle(1,HORIZ_DIR,2);
      outtextxy(510,10,"SNAKE GAME");
      delay(50);
      settextstyle(1,HORIZ_DIR,1);
       outtextxy(510,40,"POINTS:");
       outtextxy(510,80,"CONTROLS");
       outtextxy(510,120,"W=UP");
       outtextxy(510,160,"A=LEFT");
       outtextxy(510,200,"S=DOWN");
       outtextxy(510,240,"D=RIGHT");
       delay(20);
    }

  void begin()
    {   char ch;
     setcolor(WHITE);           //SNAKE
     setfillstyle(2,RED);
     circle(40,230,5);
     floodfill(40,230,WHITE);
     setcolor(BLUE);
     settextstyle(11,0,2);
     outtextxy(40,245,"SNAKE");
     delay(2000);

     setcolor(YELLOW);
     settextstyle(3,HORIZ_DIR,3);
     outtextxy(40,260,"PRESS ANY KEY TO START THE GAME");
     ch=getch();
      setcolor(BLACK);
     outtextxy(40,260,"PRESS ANY KEY TO START THE GAME");
     }



   void controls()
   { int i=40;int j=230;char c;
     int p,q,k;
     srand(time(NULL));

     p=(rand()%(480-20+1)+20);
     q=(rand()%(380-20+1)+20);
       setcolor(WHITE);
     setfillstyle(1,GREEN);     //FOOD
     circle(p,q,2);
     floodfill(p,q,WHITE);

      setcolor(WHITE);           //SNAKE
     setfillstyle(1,RED);
     circle(40,230,5);
     floodfill(40,230,WHITE);
     setcolor(BLUE);
     settextstyle(11,0,2);
     outtextxy(40,245,"SNAKE");
     delay(2000);

      setcolor(BLACK);           //erase
     setfillstyle(1,BLACK);
     circle(40,230,5);
     floodfill(40,230,BLACK);
     setcolor(BLACK);
     settextstyle(11,0,2);
     outtextxy(40,245,"SNAKE");

     for(;i<=480;i++)
     {
       setcolor(WHITE);           //newsnake
     setfillstyle(1,RED);
     circle(i,j,5);
     floodfill(i,j,WHITE);
     delay(20);
      setcolor(BLACK);           //erase
     setfillstyle(1,BLACK);
     circle(i,j,5);
     floodfill(i,j,BLACK);

      if(kbhit())
      { c=getch();
      break;
      }
      }
   again:
      switch(c)
      { case 'w':
	case 'W': for(; j>=20; j--)
		  {
		    setcolor(WHITE);           //newsnake
		   setfillstyle(1,RED);
		 circle(i,j,5);
		  floodfill(i,j,WHITE);
		  delay(20);
		  setcolor(BLACK);           //erase
		  setfillstyle(1,BLACK);
		  circle(i,j,5);
		  floodfill(i,j,BLACK);

		  if(kbhit())
		  {c=getch();
		  if(c!='w'&&c!='W')
		   goto again;
		  else if(i==p&&j==q)
		  {	score();
			p=(rand()%(480-20+1)+20);
			   q=(rand()%(380-20+1)+20);
			   setcolor(WHITE);
			     setfillstyle(1,GREEN);     //FOOD
			     circle(p,q,2);
			     floodfill(p,q,WHITE);

		   }
		  }}
		  break;

	 case 's':
	case 'S': for(; j<=390; j++)
		  {

		    setcolor(WHITE);           //newsnake
		   setfillstyle(1,RED);
		 circle(i,j,5);
		  floodfill(i,j,WHITE);
		  delay(20);
		  setcolor(BLACK);           //erase
		  setfillstyle(1,BLACK);
		  circle(i,j,5);
		  floodfill(i,j,BLACK);

		  if(kbhit())
		  {c=getch();
		  if(c!='s'&&c!='S')
		  {
		   goto again;
		   }
		  }}
		  break;

	 case 'd':
	case 'D': for(; i<=495; i++)
		  {

		    setcolor(WHITE);           //newsnake
		   setfillstyle(1,RED);
		 circle(i,j,5);
		  floodfill(i,j,WHITE);
		  delay(20);
		  setcolor(BLACK);           //erase
		  setfillstyle(1,BLACK);
		  circle(i,j,5);
		  floodfill(i,j,BLACK);

		  if(kbhit())
		  {c=getch();
		  if(c!='d'&&c!='D')
		  {
		   goto again;
		   }
		  }}
		  break;

	 case 'a':
	case 'A': for(; i>=20; i--)
		  {

		    setcolor(WHITE);           //newsnake
		   setfillstyle(1,RED);
		 circle(i,j,5);
		  floodfill(i,j,WHITE);
		  delay(20);
		  setcolor(BLACK);           //erase
		  setfillstyle(1,BLACK);
		  circle(i,j,5);
		  floodfill(i,j,BLACK);

		  if(kbhit())
		  {c=getch();
		  if(c!='a'&&c!='A')
		  {
		   goto again;
		   }
		  }}
		  break;

       }
	}

      void score()
		{ int s;
		  s+=10;
		  setcolor(YELLOW);
		  settextstyle(7,0,1);
		  outtextxy(610,40,"asdf");
		 }




 void closing()
  {

   setcolor(YELLOW);
   settextstyle(7,HORIZ_DIR,4);
   outtextxy(160,180,"!!  THANK YOU   !!");
   outtextxy(120,430," BUILT BY KULDEEP KUMAR");
  }

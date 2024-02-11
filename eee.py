import turtle
import math
Step 2: Choose a background color for your output screen. You can choose any color, we will use yellow color just to make it attractive.


screen = turtle.Screen()
screen.bgcolor("yellow")
Step 3: Choose the color and speed of your turtle(pen) who will draw the house on the screen.

t.color("black")
t.shape("turtle")
t.speed(1)
Step 4: Now, we need to draw the base of your house and for that, you need to draw a rectangle.

You can fill any color in your of your choice just by changing the color name in the t.fillcolor(‘ ‘) command. 

t.fillcolor('cyan')
t.begin_fill( )
t.right(90)
t.forward(250)
t.left(90)
t.forward(400)
t.left(90)

t.forward(250)

t.left(90)
t.forward(400)
t.right(90)
t.end_fill()
The base of the house will look this:

Video Player

00:00
00:15


Step 5: Now you created the base, the next step is to create the top of the house. Draw a triangle for the upper portion, just to keep it simple.

# for creating triangle
# i.e top of the house
t.fillcolor('brown')
t.begin_fill()
t.right(45)
t.forward(200)
t.right(90)
t.forward(200)
t.left(180)
t.forward(200)
t.right(135)
t.forward(259)
t.right(90)
t.forward(142)
t.end_fill()

Step 6: We must secure our house by Putting the Door and also windows for ventilation. Here is the code for that-

# for windows and
# for creating door
t.right(90)
t.forward(400)
t.left(90)
t.forward(50)
t.left(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(180)
t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)
t.right(90)
t.forward(200)
t.right(90)
t.forward(150)

t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(200)

Complete Code:

import turtle 
  
  
t = turtle.Turtle() 
  
# for background 
screen = turtle.Screen() 
screen.bgcolor("yellow") 
  
#color and speed 
# of turtle 
# creating the house 
t.color("black") 
t.shape("turtle") 
t.speed(1) 
  
# for creating base of 
# the house 
t.fillcolor('cyan') 
t.begin_fill() 
t.right(90) 
t.forward(250) 
t.left(90) 
t.forward(400) 
t.left(90) 
t.forward(250) 
t.left(90) 
t.forward(400) 
t.right(90) 
t.end_fill() 
  
# for top of 
# the house 
t.fillcolor('brown') 
t.begin_fill() 
t.right(45) 
t.forward(200) 
t.right(90) 
t.forward(200) 
t.left(180) 
t.forward(200) 
t.right(135) 
t.forward(259) 
t.right(90) 
t.forward(142) 
t.end_fill() 
  
# for door and 
# windows 
t.right(90) 
t.forward(400) 
t.left(90) 
t.forward(50) 
t.left(90) 
t.forward(150) 
t.right(90) 
t.forward(200) 
t.right(180) 
t.forward(200) 
t.right(90) 
t.forward(200) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(200) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(100) 
t.right(90) 
t.forward(150) 
t.right(90) 
t.forward(100) 
t.right(90) 
t.forward(75) 
t.right(90) 
t.forward(200) 
t.right(180) 
t.forward(200) 
t.right(90) 
t.forward(75) 
t.left(90) 
t.forward(15) 
t.left(90) 
t.forward(200) 
t.right(90) 
t.forward(15) 
t.right(90) 
t.forward(75) 
Output:

Video Player

00:00
00:45



Don't miss your chance to ride the wave of the data revolution! Every industry is scaling new heights by tapping into the power of data. Sharpen your skills and become a part of the hottest trend in the 21st century.

Dive into the future of technology - explore the Complete Machine Learning and Data Science Program by GeeksforGeeks and stay ahead of the curve.


Commit to GfG's Three-90 Challenge! Purchase a course, complete 90% in 90 days, and save 90% cost click here to explore.
Last Updated : 01 Oct, 2020

7

Previous
Draw Color Filled Shapes in Turtle - Python
Next
Ternary contours Plot using Plotly in Python
Share your thoughts in the comments

Add Your Comment
Similar Reads
Draw Circle in Python using Turtle
Draw a Hut using turtle module in Python
Python - Draw Hexagon Using Turtle Graphics
Python - Draw Star Using Turtle Graphics
Python - Draw Octagonal shape Using Turtle Graphics
Draw a Tic Tac Toe Board using Python-Turtle
Draw Cube and Cuboid in Python using Turtle
Draw Shape inside Shape in Python Using Turtle
Draw Colored Solid Cube using Turtle in Python
Draw smiling face emoji using Turtle in Python
Complete Tutorials
Python Crash Course
Python API Tutorial: Getting Started with APIs
Advanced Python Tutorials
Python Automation Tutorial
OpenAI Python API - Complete Guide
A

anshitaagarwal
Article Tags :
Python-turtle 
Python
Practice Tags :
python
Additional Information
Trending in News
View More
Top 7 AI Tools for Healthcare Professionals in 2024
Top 10 AI Tools for Podcasters: Exclusive List [2024]
How To Make QR Code Art Using AI
Top 7 AI Tools for Video Game Development in 2024
10 Best Free AI Art Generators to Create Image From Text [Free & Paid]

geeksforgeeks-footer-logo
A-143, 9th Floor, Sovereign Corporate Tower, Sector-136, Noida, Uttar Pradesh - 201305
GFG App on Play Store
GFG App on App Store
Company
About Us
Legal
Careers
In Media
Contact Us
Advertise with us
GFG Corporate Solution
Placement Training Program
Apply for Mentor
Explore
Job-A-Thon Hiring Challenge
Hack-A-Thon
GfG Weekly Contest
Offline Classes (Delhi/NCR)
DSA in JAVA/C++
Master System Design
Master CP
GeeksforGeeks Videos
Geeks Community
Languages
Python
Java
C++
PHP
GoLang
SQL
R Language
Android Tutorial
Tutorials Archive
DSA
Data Structures
Algorithms
DSA for Beginners
Basic DSA Problems
DSA Roadmap
Top 100 DSA Interview Problems
DSA Roadmap by Sandeep Jain
All Cheat Sheets
Data Science & ML
Data Science With Python
Data Science For Beginner
Machine Learning Tutorial
ML Maths
Data Visualisation Tutorial
Pandas Tutorial
NumPy Tutorial
NLP Tutorial
Deep Learning Tutorial
HTML & CSS
HTML
CSS
Web Templates
CSS Frameworks
Bootstrap
Tailwind CSS
SASS
LESS
Web Design
Python
Python Programming Examples
Django Tutorial
Python Projects
Python Tkinter
Web Scraping
OpenCV Python Tutorial
Python Interview Question
Computer Science
GATE CS Notes
Operating Systems
Computer Network
Database Management System
Software Engineering
Digital Logic Design
Engineering Maths
DevOps
Git
AWS
Docker
Kubernetes
Azure
GCP
DevOps Roadmap
Competitive Programming
Top DS or Algo for CP
Top 50 Tree
Top 50 Graph
Top 50 Array
Top 50 String
Top 50 DP
Top 15 Websites for CP
System Design
High Level Design
Low Level Design
UML Diagrams
Interview Guide
Design Patterns
OOAD
System Design Bootcamp
Interview Questions
JavaScript
JavaScript Examples
TypeScript
ReactJS
NextJS
AngularJS
NodeJS
Lodash
Web Browser
NCERT Solutions
Class 12
Class 11
Class 10
Class 9
Class 8
Complete Study Material
School Subjects
Mathematics
Physics
Chemistry
Biology
Social Science
English Grammar
Commerce
Accountancy
Business Studies
Indian Economics
Macroeconomics
Microeconimics
Statistics for Economics
Management & Finance
Management
HR Managament
Income Tax
Finance
Economics
UPSC Study Material
Polity Notes
Geography Notes
History Notes
Science and Technology Notes
Economy Notes
Ethics Notes
Previous Year Papers
SSC/ BANKING
SSC CGL Syllabus
SBI PO Syllabus
SBI Clerk Syllabus
IBPS PO Syllabus
IBPS Clerk Syllabus
SSC CGL Practice Papers
Colleges
Indian Colleges Admission & Campus Experiences
List of Central Universities - In India
Colleges in Delhi University
IIT Colleges
NIT Colleges
IIIT Colleges
Companies
IT Companies
Software Development Companies
Artificial Intelligence(AI) Companies
CyberSecurity Companies



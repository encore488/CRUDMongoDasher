To run this project in Linux: download the zip file and the csv file at the top. Download MongoDB 

Open a linux terminal and use it to upload the csv file into a mongo database called animals with these commands as your guide:  /usr/local/datasets
mongoimport --username="${MONGO_USER}" \
    --password="${MONGO_PASS}" --port=${MONGO_PORT} \
    --host=${MONGO_HOST} --db AAC --collection animals \ 
    --authenticationDatabase admin --drop ./aac_shelter_outcomes.csv
Now, the .py file should be able to access the csv file to read it and perform aperations on it, but you may need to alter the path set in the .py file to fit your path. 
The final step is to run the Jupyter Notebook (the ipynb file within the .zip file.)



How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?


To create a program that is maintainable or adaptable, documantation and clear comments is key. If someone who doesn't know much about the technology you're using can read the documentation and comments and understand how it all works, then that is an indicator that the project is maintainable. Another key is writing code that isn't unnecessarily complex or reliant on too many other libraries and niche products so that the project doesn't need updated to accomodate every change to the libraries it relies on.


How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?


One of the first steps in solving a problem in computer science is to write down some rough pseudocode of what you want to accomplish. This forces you to think about the problem from a big picture perspective before you get lost in the details. Then, I would think about the technologies necessary to do this and start getting some basic knowledge on those tools by watching youtube videos, then reading documentation for the functions you think are going to be useful. Then, more detailed pseudocode may be in order, or you could skip that for a simple program and jump straight into coding. Never forget that you should try to run and check and debug code as often as possible, so that you don't do a huge chunk of work only to find that it is full of hard to pinpoint errors that interfere with each other.


What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?


Computer scientist do research into a wide range of topics that all have to do with computers. Some questions they answer are things like "How can we get many processors to cooperate at solving a task?" and "What problems are theoretically impossible for a computer to solve?" These things mattter because they lay the groundwork for software engineers and other computer experts to implement new and improved solutions to existing problems. The advancement of computer science is necessary for increasing efficiency at many of our activities and unlocking new abilities that used to be impossible (like autoated driving.)
My work could help a company to focus on the data that they really need to know about. I can filter out all the noise and create a presentable dashboard that allows a user to better understand the information that they need to see. In other words, I can take a big mess of data and turn it into an interactive, comprehensible format that a non-technical person can use and understand.

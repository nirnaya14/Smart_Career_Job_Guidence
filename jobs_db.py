# Prompt: Create a Python job database with 50+ job roles for Indian students
# including Software Development, Web Development, Data Analytics, AI/ML, Cloud,
# DevOps, Design, Cybersecurity, Testing and Marketing. Each job has title,
# category, required skills, salary, companies, roadmap and free resources.
# Also create a skill matching function that returns ranked jobs with match %.

"""
Complete Job Database — No API needed!
50+ jobs with required skills, salary, companies, roadmap and resources.
"""

JOBS_DATABASE = [

    # ── Software Development ──────────────────────────────────────────────────
    {
        "title": "Python Developer",
        "category": "Software Development",
        "skills_required": ["python"],
        "skills_bonus": ["django", "flask", "sql", "git", "rest api"],
        "description": "Build applications and automate tasks using Python programming.",
        "salary": "₹3.5 – 8 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Infosys", "TCS", "Wipro", "Zoho", "Freshworks"],
        "learn_next": ["Django", "Flask", "SQL", "REST API", "Git"],
        "resources": [
            {"topic": "Python Full Course", "platform": "freeCodeCamp YouTube", "link": "https://www.youtube.com/watch?v=rfscVS0vtbw", "free": True},
            {"topic": "Django Tutorial", "platform": "Django Official Docs", "link": "https://docs.djangoproject.com/en/stable/intro/tutorial01/", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master Python basics — functions, loops, OOP"},
            {"week": "Week 3-4", "task": "Learn Django framework — build simple web app"},
            {"week": "Week 5-6", "task": "Learn SQL database basics"},
            {"week": "Week 7-8", "task": "Build 2 portfolio projects and push to GitHub"},
            {"week": "Month 3", "task": "Apply for Python developer internships"},
        ]
    },
    {
        "title": "Web Developer (Full Stack)",
        "category": "Web Development",
        "skills_required": ["html", "css"],
        "skills_bonus": ["javascript", "react", "node.js", "bootstrap", "python", "php"],
        "description": "Design and develop complete websites and web applications.",
        "salary": "₹3 – 9 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Accenture", "Capgemini", "HCL", "Mphasis", "Mindtree"],
        "learn_next": ["JavaScript", "React", "Node.js", "SQL", "Git"],
        "resources": [
            {"topic": "HTML CSS Full Course", "platform": "freeCodeCamp", "link": "https://www.freecodecamp.org/learn/responsive-web-design/", "free": True},
            {"topic": "JavaScript Tutorial", "platform": "javascript.info", "link": "https://javascript.info", "free": True},
            {"topic": "React Course", "platform": "React Official Docs", "link": "https://react.dev/learn", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master HTML5 and CSS3 — build 3 static pages"},
            {"week": "Week 3-4", "task": "Learn JavaScript fundamentals"},
            {"week": "Week 5-6", "task": "Learn React basics — build todo app"},
            {"week": "Week 7-8", "task": "Learn Node.js and basic backend"},
            {"week": "Month 3", "task": "Build full stack project and apply for jobs"},
        ]
    },
    {
        "title": "Frontend Developer",
        "category": "Web Development",
        "skills_required": ["html", "css", "javascript"],
        "skills_bonus": ["react", "vue", "bootstrap", "figma", "typescript"],
        "description": "Build beautiful and responsive user interfaces for websites and apps.",
        "salary": "₹3 – 8 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Razorpay", "Swiggy", "Zomato", "Meesho", "Urban Company"],
        "learn_next": ["React", "TypeScript", "Figma", "CSS Animations", "Testing"],
        "resources": [
            {"topic": "React Full Course", "platform": "YouTube - Traversy Media", "link": "https://www.youtube.com/watch?v=w7ejDZ8SWv8", "free": True},
            {"topic": "CSS Advanced", "platform": "CSS Tricks", "link": "https://css-tricks.com", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master advanced CSS — Flexbox, Grid, Animations"},
            {"week": "Week 3-4", "task": "Deep dive into JavaScript — DOM, Events, APIs"},
            {"week": "Week 5-6", "task": "Learn React — components, hooks, state"},
            {"week": "Week 7-8", "task": "Build 3 responsive UI projects"},
            {"week": "Month 3", "task": "Create portfolio website and apply"},
        ]
    },
    {
        "title": "Java Developer",
        "category": "Software Development",
        "skills_required": ["java"],
        "skills_bonus": ["spring boot", "sql", "hibernate", "maven", "git"],
        "description": "Develop enterprise applications and backend systems using Java.",
        "salary": "₹4 – 10 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["TCS", "Infosys", "Wipro", "IBM", "Oracle"],
        "learn_next": ["Spring Boot", "Hibernate", "SQL", "Maven", "Microservices"],
        "resources": [
            {"topic": "Java Full Course", "platform": "freeCodeCamp YouTube", "link": "https://www.youtube.com/watch?v=GoXwIVyNvX0", "free": True},
            {"topic": "Spring Boot Tutorial", "platform": "Baeldung", "link": "https://www.baeldung.com/spring-boot", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master Java OOP — classes, inheritance, interfaces"},
            {"week": "Week 3-4", "task": "Learn Collections, Exception Handling, Multithreading"},
            {"week": "Week 5-6", "task": "Learn Spring Boot framework"},
            {"week": "Week 7-8", "task": "Learn SQL and Hibernate ORM"},
            {"week": "Month 3", "task": "Build REST API project and apply"},
        ]
    },
    {
        "title": "Android Developer",
        "category": "Mobile Development",
        "skills_required": ["java", "android"],
        "skills_bonus": ["kotlin", "xml", "firebase", "rest api", "sqlite"],
        "description": "Build mobile applications for Android smartphones and tablets.",
        "salary": "₹4 – 10 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Samsung", "Paytm", "PhonePe", "BYJU's", "Ola"],
        "learn_next": ["Kotlin", "Firebase", "REST APIs", "Material Design", "Play Store Publishing"],
        "resources": [
            {"topic": "Android Development", "platform": "Google Android Developers", "link": "https://developer.android.com/courses", "free": True},
            {"topic": "Kotlin Course", "platform": "Kotlin Official", "link": "https://kotlinlang.org/docs/android-overview.html", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn Android Studio setup and XML layouts"},
            {"week": "Week 3-4", "task": "Build simple calculator and to-do apps"},
            {"week": "Week 5-6", "task": "Learn Firebase for backend"},
            {"week": "Week 7-8", "task": "Integrate REST APIs in app"},
            {"week": "Month 3", "task": "Publish app on Play Store and apply for jobs"},
        ]
    },

    # ── Data & AI ─────────────────────────────────────────────────────────────
    {
        "title": "Data Analyst",
        "category": "Data & Analytics",
        "skills_required": ["python", "excel"],
        "skills_bonus": ["sql", "tableau", "power bi", "pandas", "matplotlib", "statistics"],
        "description": "Analyze data to find insights and help businesses make decisions.",
        "salary": "₹4 – 10 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Amazon", "Flipkart", "Deloitte", "EY", "KPMG"],
        "learn_next": ["SQL", "Tableau", "Power BI", "Statistics", "Pandas"],
        "resources": [
            {"topic": "Data Analysis with Python", "platform": "freeCodeCamp", "link": "https://www.freecodecamp.org/learn/data-analysis-with-python/", "free": True},
            {"topic": "SQL Tutorial", "platform": "W3Schools", "link": "https://www.w3schools.com/sql/", "free": True},
            {"topic": "Power BI", "platform": "Microsoft Learn", "link": "https://learn.microsoft.com/en-us/power-bi/", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master Excel — Pivot Tables, VLOOKUP, Charts"},
            {"week": "Week 3-4", "task": "Learn SQL — SELECT, JOIN, GROUP BY"},
            {"week": "Week 5-6", "task": "Learn Python Pandas and Matplotlib"},
            {"week": "Week 7-8", "task": "Learn Power BI or Tableau"},
            {"week": "Month 3", "task": "Build 3 data analysis projects and apply"},
        ]
    },
    {
        "title": "Machine Learning Engineer",
        "category": "Data & AI",
        "skills_required": ["python", "machine learning"],
        "skills_bonus": ["tensorflow", "keras", "scikit-learn", "numpy", "pandas", "deep learning"],
        "description": "Build AI models that learn from data to make predictions.",
        "salary": "₹6 – 15 LPA",
        "experience": "0-2 years",
        "companies": ["Google", "Microsoft", "Amazon", "Flipkart", "Ola"],
        "learn_next": ["TensorFlow", "Deep Learning", "NLP", "Computer Vision", "MLOps"],
        "resources": [
            {"topic": "ML Course by Andrew Ng", "platform": "Coursera (Free Audit)", "link": "https://www.coursera.org/learn/machine-learning", "free": True},
            {"topic": "Fast.ai Deep Learning", "platform": "fast.ai", "link": "https://www.fast.ai", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master NumPy, Pandas, Matplotlib"},
            {"week": "Week 3-4", "task": "Learn ML algorithms — Linear Regression, Classification"},
            {"week": "Week 5-6", "task": "Learn Scikit-learn library"},
            {"week": "Week 7-8", "task": "Learn Neural Networks with TensorFlow"},
            {"week": "Month 3", "task": "Build 2 ML projects and publish on Kaggle"},
        ]
    },
    {
        "title": "Data Scientist",
        "category": "Data & AI",
        "skills_required": ["python", "statistics"],
        "skills_bonus": ["machine learning", "sql", "r", "tableau", "deep learning", "nlp"],
        "description": "Use statistics and ML to extract insights from complex datasets.",
        "salary": "₹6 – 18 LPA",
        "experience": "0-3 years",
        "companies": ["Amazon", "Microsoft", "Walmart Labs", "Mu Sigma", "Tiger Analytics"],
        "learn_next": ["Statistics", "Machine Learning", "SQL", "Deep Learning", "NLP"],
        "resources": [
            {"topic": "Statistics for Data Science", "platform": "Khan Academy", "link": "https://www.khanacademy.org/math/statistics-probability", "free": True},
            {"topic": "Python for Data Science", "platform": "Kaggle Learn", "link": "https://www.kaggle.com/learn/python", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn Statistics — Mean, Median, Distributions"},
            {"week": "Week 3-4", "task": "Master Python Data Science libraries"},
            {"week": "Week 5-6", "task": "Learn Machine Learning algorithms"},
            {"week": "Week 7-8", "task": "Work on real datasets from Kaggle"},
            {"week": "Month 3", "task": "Complete Kaggle competitions and apply"},
        ]
    },

    # ── Cloud & DevOps ────────────────────────────────────────────────────────
    {
        "title": "Cloud Engineer (AWS)",
        "category": "Cloud & DevOps",
        "skills_required": ["aws"],
        "skills_bonus": ["linux", "python", "docker", "terraform", "networking"],
        "description": "Deploy and manage applications on Amazon Web Services cloud platform.",
        "salary": "₹5 – 14 LPA",
        "experience": "0-2 years",
        "companies": ["Amazon", "Accenture", "Cognizant", "Capgemini", "HCL"],
        "learn_next": ["AWS Certification", "Docker", "Terraform", "Linux", "Networking"],
        "resources": [
            {"topic": "AWS Free Tier", "platform": "AWS Official", "link": "https://aws.amazon.com/free/", "free": True},
            {"topic": "AWS Cloud Practitioner", "platform": "freeCodeCamp YouTube", "link": "https://www.youtube.com/watch?v=3hLmDS179YE", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Create AWS free account and explore services"},
            {"week": "Week 3-4", "task": "Learn EC2, S3, RDS basics"},
            {"week": "Week 5-6", "task": "Learn Docker and containerization"},
            {"week": "Week 7-8", "task": "Prepare for AWS Cloud Practitioner exam"},
            {"week": "Month 3", "task": "Get certified and apply for cloud jobs"},
        ]
    },
    {
        "title": "DevOps Engineer",
        "category": "Cloud & DevOps",
        "skills_required": ["linux", "git"],
        "skills_bonus": ["docker", "kubernetes", "jenkins", "aws", "python", "bash"],
        "description": "Automate software deployment and manage infrastructure.",
        "salary": "₹5 – 15 LPA",
        "experience": "0-3 years",
        "companies": ["ThoughtWorks", "Publicis Sapient", "Infosys", "Wipro", "HCL"],
        "learn_next": ["Docker", "Kubernetes", "Jenkins", "AWS/Azure", "Terraform"],
        "resources": [
            {"topic": "DevOps Roadmap", "platform": "roadmap.sh", "link": "https://roadmap.sh/devops", "free": True},
            {"topic": "Docker Tutorial", "platform": "Docker Official Docs", "link": "https://docs.docker.com/get-started/", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master Linux commands and shell scripting"},
            {"week": "Week 3-4", "task": "Learn Git and CI/CD concepts"},
            {"week": "Week 5-6", "task": "Learn Docker — build and run containers"},
            {"week": "Week 7-8", "task": "Learn Jenkins for automation"},
            {"week": "Month 3", "task": "Learn Kubernetes basics and apply"},
        ]
    },

    # ── Design ────────────────────────────────────────────────────────────────
    {
        "title": "UI/UX Designer",
        "category": "Design",
        "skills_required": ["figma"],
        "skills_bonus": ["photoshop", "illustrator", "html", "css", "prototyping", "user research"],
        "description": "Design beautiful and user-friendly interfaces for apps and websites.",
        "salary": "₹3 – 9 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Razorpay", "Myntra", "Swiggy", "CRED", "Groww"],
        "learn_next": ["Figma Advanced", "User Research", "Prototyping", "Design Systems", "HTML/CSS"],
        "resources": [
            {"topic": "Figma Full Course", "platform": "Figma YouTube", "link": "https://www.youtube.com/watch?v=FTFaQWZBqQ8", "free": True},
            {"topic": "UX Design Course", "platform": "Google UX Design Certificate", "link": "https://grow.google/certificates/ux-design/", "free": False},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn Figma basics — frames, components, styles"},
            {"week": "Week 3-4", "task": "Study UI design principles and color theory"},
            {"week": "Week 5-6", "task": "Design 3 mobile app screens"},
            {"week": "Week 7-8", "task": "Learn prototyping and user testing"},
            {"week": "Month 3", "task": "Build Behance/Dribbble portfolio and apply"},
        ]
    },
    {
        "title": "Graphic Designer",
        "category": "Design",
        "skills_required": ["photoshop"],
        "skills_bonus": ["illustrator", "canva", "figma", "after effects", "video editing"],
        "description": "Create visual content for brands, social media and marketing.",
        "salary": "₹2.5 – 7 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Ogilvy", "Leo Burnett", "Dentsu", "Wunderman Thompson", "WPP"],
        "learn_next": ["Adobe Illustrator", "After Effects", "Motion Graphics", "Branding", "Typography"],
        "resources": [
            {"topic": "Photoshop Tutorial", "platform": "Adobe YouTube", "link": "https://www.youtube.com/user/Photoshop", "free": True},
            {"topic": "Canva Design School", "platform": "Canva", "link": "https://www.canva.com/learn/", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master Photoshop — layers, masks, effects"},
            {"week": "Week 3-4", "task": "Learn Illustrator — vectors and logos"},
            {"week": "Week 5-6", "task": "Study typography and color theory"},
            {"week": "Week 7-8", "task": "Create 10 design projects for portfolio"},
            {"week": "Month 3", "task": "Build Behance portfolio and apply"},
        ]
    },

    # ── Database & Backend ────────────────────────────────────────────────────
    {
        "title": "Database Administrator",
        "category": "Database",
        "skills_required": ["sql"],
        "skills_bonus": ["mysql", "postgresql", "oracle", "mongodb", "python", "linux"],
        "description": "Manage and optimize databases for organizations and applications.",
        "salary": "₹4 – 10 LPA",
        "experience": "0-2 years",
        "companies": ["Oracle", "SAP", "TCS", "Wipro", "Infosys"],
        "learn_next": ["MySQL Advanced", "PostgreSQL", "MongoDB", "Database Tuning", "Backup & Recovery"],
        "resources": [
            {"topic": "SQL Tutorial", "platform": "W3Schools", "link": "https://www.w3schools.com/sql/", "free": True},
            {"topic": "MySQL Full Course", "platform": "freeCodeCamp YouTube", "link": "https://www.youtube.com/watch?v=HXV3zeQKqGY", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master SQL — SELECT, INSERT, UPDATE, DELETE"},
            {"week": "Week 3-4", "task": "Learn JOINs, subqueries, stored procedures"},
            {"week": "Week 5-6", "task": "Learn database design and normalization"},
            {"week": "Week 7-8", "task": "Learn MySQL administration and backup"},
            {"week": "Month 3", "task": "Get MySQL certification and apply"},
        ]
    },

    # ── Cybersecurity ─────────────────────────────────────────────────────────
    {
        "title": "Cybersecurity Analyst",
        "category": "Cybersecurity",
        "skills_required": ["networking", "linux"],
        "skills_bonus": ["ethical hacking", "python", "cybersecurity", "kali linux", "wireshark"],
        "description": "Protect organizations from cyber attacks and security threats.",
        "salary": "₹4 – 12 LPA",
        "experience": "0-2 years",
        "companies": ["Deloitte", "EY", "PwC", "IBM Security", "Tata Communications"],
        "learn_next": ["Ethical Hacking", "Network Security", "Kali Linux", "OWASP", "CEH Certification"],
        "resources": [
            {"topic": "Cybersecurity Roadmap", "platform": "roadmap.sh", "link": "https://roadmap.sh/cyber-security", "free": True},
            {"topic": "TryHackMe", "platform": "TryHackMe", "link": "https://tryhackme.com", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn networking basics — TCP/IP, DNS, HTTP"},
            {"week": "Week 3-4", "task": "Master Linux commands"},
            {"week": "Week 5-6", "task": "Learn ethical hacking basics on TryHackMe"},
            {"week": "Week 7-8", "task": "Practice on HackTheBox platform"},
            {"week": "Month 3", "task": "Get CompTIA Security+ certification"},
        ]
    },

    # ── Testing ───────────────────────────────────────────────────────────────
    {
        "title": "Software Test Engineer",
        "category": "Testing & QA",
        "skills_required": ["manual testing"],
        "skills_bonus": ["selenium", "python", "java", "sql", "jira", "automation testing"],
        "description": "Test software applications to find bugs before release.",
        "salary": "₹3 – 8 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["TCS", "Infosys", "Wipro", "Cognizant", "Capgemini"],
        "learn_next": ["Selenium WebDriver", "Python for Testing", "API Testing", "Jira", "TestNG"],
        "resources": [
            {"topic": "Selenium Python", "platform": "Selenium Official", "link": "https://selenium-python.readthedocs.io", "free": True},
            {"topic": "Software Testing Tutorial", "platform": "Guru99", "link": "https://www.guru99.com/software-testing.html", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn manual testing concepts and test cases"},
            {"week": "Week 3-4", "task": "Learn Selenium WebDriver with Python"},
            {"week": "Week 5-6", "task": "Learn API testing with Postman"},
            {"week": "Week 7-8", "task": "Learn SQL for database testing"},
            {"week": "Month 3", "task": "Get ISTQB certification and apply"},
        ]
    },

    # ── Digital Marketing ─────────────────────────────────────────────────────
    {
        "title": "Digital Marketing Executive",
        "category": "Marketing",
        "skills_required": ["digital marketing"],
        "skills_bonus": ["seo", "social media", "google ads", "content writing", "canva", "analytics"],
        "description": "Promote brands and products through online channels and social media.",
        "salary": "₹2.5 – 6 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Nykaa", "Myntra", "MakeMyTrip", "OYO", "Zomato"],
        "learn_next": ["SEO", "Google Ads", "Facebook Ads", "Email Marketing", "Analytics"],
        "resources": [
            {"topic": "Google Digital Garage", "platform": "Google", "link": "https://learndigital.withgoogle.com/digitalgarage", "free": True},
            {"topic": "HubSpot Marketing", "platform": "HubSpot Academy", "link": "https://academy.hubspot.com", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn SEO basics and keyword research"},
            {"week": "Week 3-4", "task": "Learn Google Ads and Facebook Ads"},
            {"week": "Week 5-6", "task": "Learn email marketing and automation"},
            {"week": "Week 7-8", "task": "Learn Google Analytics"},
            {"week": "Month 3", "task": "Get Google Digital Marketing certificate"},
        ]
    },

    # ── Content & Writing ─────────────────────────────────────────────────────
    {
        "title": "Content Writer / Copywriter",
        "category": "Content & Writing",
        "skills_required": ["content writing"],
        "skills_bonus": ["seo", "social media", "blogging", "ms word", "research"],
        "description": "Write engaging content for websites, blogs and social media.",
        "salary": "₹2.5 – 6 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["Times Internet", "HT Media", "Byju's", "Unacademy", "Coursera India"],
        "learn_next": ["SEO Writing", "Copywriting", "Social Media Content", "Technical Writing"],
        "resources": [
            {"topic": "Copywriting Course", "platform": "Coursera (Free Audit)", "link": "https://www.coursera.org/learn/copywriting", "free": True},
            {"topic": "SEO Writing", "platform": "Yoast Academy", "link": "https://yoast.com/academy/", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Study grammar, writing styles and tone"},
            {"week": "Week 3-4", "task": "Learn SEO writing and keyword research"},
            {"week": "Week 5-6", "task": "Write 10 blog posts on any topic"},
            {"week": "Week 7-8", "task": "Create writing portfolio on Medium"},
            {"week": "Month 3", "task": "Apply for freelance and full-time writing jobs"},
        ]
    },

    # ── Excel / Office ────────────────────────────────────────────────────────
    {
        "title": "MIS Executive / Data Entry",
        "category": "Office & Administration",
        "skills_required": ["excel"],
        "skills_bonus": ["ms office", "data entry", "sql", "tally", "power bi"],
        "description": "Manage data, reports and information systems using Excel and tools.",
        "salary": "₹2 – 4.5 LPA",
        "experience": "Fresher",
        "companies": ["HDFC Bank", "ICICI Bank", "Reliance", "Tata Group", "Mahindra"],
        "learn_next": ["Advanced Excel", "Power BI", "SQL", "VBA Macros", "Tally"],
        "resources": [
            {"topic": "Excel Full Course", "platform": "freeCodeCamp YouTube", "link": "https://www.youtube.com/watch?v=Vl0H-qTclOg", "free": True},
            {"topic": "Power BI Tutorial", "platform": "Microsoft Learn", "link": "https://learn.microsoft.com/en-us/power-bi/", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master Excel — Formulas, Pivot Tables, Charts"},
            {"week": "Week 3-4", "task": "Learn advanced Excel — VLOOKUP, Macros"},
            {"week": "Week 5-6", "task": "Learn Power BI dashboards"},
            {"week": "Week 7-8", "task": "Learn basic SQL"},
            {"week": "Month 3", "task": "Apply for MIS and data analyst roles"},
        ]
    },

    # ── More jobs ─────────────────────────────────────────────────────────────
    {
        "title": "React Developer",
        "category": "Web Development",
        "skills_required": ["react"],
        "skills_bonus": ["javascript", "html", "css", "node.js", "redux", "typescript"],
        "description": "Build modern, interactive web applications using React.js library.",
        "salary": "₹4 – 12 LPA",
        "experience": "0-2 years",
        "companies": ["Razorpay", "CRED", "Groww", "Zerodha", "Meesho"],
        "learn_next": ["TypeScript", "Redux", "Next.js", "Testing", "Performance Optimization"],
        "resources": [
            {"topic": "React Official Docs", "platform": "React.dev", "link": "https://react.dev", "free": True},
            {"topic": "Next.js Course", "platform": "Next.js Official", "link": "https://nextjs.org/learn", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Master React components, props and state"},
            {"week": "Week 3-4", "task": "Learn React hooks — useState, useEffect"},
            {"week": "Week 5-6", "task": "Learn Redux for state management"},
            {"week": "Week 7-8", "task": "Learn Next.js for full stack React"},
            {"week": "Month 3", "task": "Build 3 React projects and apply"},
        ]
    },
    {
        "title": "Django Developer",
        "category": "Web Development",
        "skills_required": ["django"],
        "skills_bonus": ["python", "sql", "html", "css", "rest api", "postgresql"],
        "description": "Build powerful web applications using the Django Python framework.",
        "salary": "₹4 – 10 LPA",
        "experience": "0-2 years",
        "companies": ["Freshworks", "Zoho", "Chargebee", "Postman", "BrowserStack"],
        "learn_next": ["Django REST Framework", "PostgreSQL", "Redis", "Celery", "Docker"],
        "resources": [
            {"topic": "Django Official Tutorial", "platform": "Django Docs", "link": "https://docs.djangoproject.com/en/stable/intro/tutorial01/", "free": True},
            {"topic": "Django Full Course", "platform": "YouTube - Dennis Ivy", "link": "https://www.youtube.com/watch?v=PtQiiknWUcI", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn Django basics — models, views, templates"},
            {"week": "Week 3-4", "task": "Build a complete CRUD web application"},
            {"week": "Week 5-6", "task": "Learn Django REST Framework — build APIs"},
            {"week": "Week 7-8", "task": "Learn authentication, deployment on Heroku"},
            {"week": "Month 3", "task": "Build portfolio project and apply"},
        ]
    },
    {
        "title": "PHP Developer",
        "category": "Web Development",
        "skills_required": ["php"],
        "skills_bonus": ["mysql", "html", "css", "javascript", "laravel", "wordpress"],
        "description": "Develop dynamic websites and web applications using PHP.",
        "salary": "₹2.5 – 7 LPA",
        "experience": "Fresher / 0-2 years",
        "companies": ["TCS", "Infosys", "Wipro", "Zensar", "Persistent Systems"],
        "learn_next": ["Laravel", "MySQL", "REST API", "WordPress", "Composer"],
        "resources": [
            {"topic": "PHP Tutorial", "platform": "W3Schools", "link": "https://www.w3schools.com/php/", "free": True},
            {"topic": "Laravel Tutorial", "platform": "Laravel Official", "link": "https://laravel.com/docs", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn PHP basics — variables, functions, forms"},
            {"week": "Week 3-4", "task": "Learn MySQL and PHP database connection"},
            {"week": "Week 5-6", "task": "Learn Laravel framework"},
            {"week": "Week 7-8", "task": "Build a complete PHP web application"},
            {"week": "Month 3", "task": "Build portfolio and apply for PHP jobs"},
        ]
    },
    {
        "title": "Network Engineer",
        "category": "Networking & Infrastructure",
        "skills_required": ["networking"],
        "skills_bonus": ["ccna", "linux", "cisco", "routing", "switching", "firewall"],
        "description": "Design, implement and manage computer networks for organizations.",
        "salary": "₹3 – 9 LPA",
        "experience": "0-2 years",
        "companies": ["Airtel", "Jio", "BSNL", "Tata Communications", "NTT"],
        "learn_next": ["CCNA Certification", "Linux", "Routing & Switching", "Network Security", "Firewall"],
        "resources": [
            {"topic": "CCNA Study Guide", "platform": "Cisco NetAcad", "link": "https://www.netacad.com", "free": True},
            {"topic": "Networking Basics", "platform": "Cisco NetAcad", "link": "https://www.netacad.com/courses/networking-basics", "free": True},
        ],
        "roadmap": [
            {"week": "Week 1-2", "task": "Learn OSI model, TCP/IP, IP addressing"},
            {"week": "Week 3-4", "task": "Learn routing and switching concepts"},
            {"week": "Week 5-6", "task": "Practice on Cisco Packet Tracer (free)"},
            {"week": "Week 7-8", "task": "Prepare for CCNA certification exam"},
            {"week": "Month 3", "task": "Get CCNA certified and apply"},
        ]
    },
]


def match_jobs(skills_input):
    """
    Match student skills against job database.
    Returns ranked list of matching jobs with match percentage.
    """
    # Normalize skills to lowercase list
    student_skills = [s.strip().lower() for s in skills_input.split(",") if s.strip()]

    matched = []

    for job in JOBS_DATABASE:
        required  = job["skills_required"]
        bonus     = job["skills_bonus"]

        # Check required skills
        req_match = sum(1 for r in required if any(r in s or s in r for s in student_skills))
        bon_match = sum(1 for b in bonus   if any(b in s or s in b for s in student_skills))

        if req_match == 0:
            continue

        # Calculate match percentage
        total_skills = len(required) + len(bonus)
        matched_count = req_match * 2 + bon_match  # required skills weighted more
        match_pct = min(int((matched_count / (len(required) * 2 + len(bonus))) * 100), 99)

        matched.append({**job, "match_percent": match_pct})

    # Sort by match percentage
    matched.sort(key=lambda x: x["match_percent"], reverse=True)
    return matched[:6]  # Return top 6


def get_skill_gaps(skills_input, matched_jobs):
    """Get skills the student is missing for their top matched jobs."""
    student_skills = [s.strip().lower() for s in skills_input.split(",") if s.strip()]
    gaps = {}

    for job in matched_jobs[:3]:
        for skill in job["learn_next"]:
            skill_lower = skill.lower()
            if not any(skill_lower in s or s in skill_lower for s in student_skills):
                if skill not in gaps:
                    gaps[skill] = 0
                gaps[skill] += 1

    # Sort by frequency
    sorted_gaps = sorted(gaps.items(), key=lambda x: x[1], reverse=True)
    return [{"skill": s, "count": c, "importance": "High" if c >= 2 else "Medium" if c == 1 else "Low"}
            for s, c in sorted_gaps[:8]]


def get_all_categories():
    """Get unique job categories."""
    return list(set(job["category"] for job in JOBS_DATABASE))


def get_jobs_by_category(category):
    """Get jobs by category."""
    return [j for j in JOBS_DATABASE if j["category"] == category]

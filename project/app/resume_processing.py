import spacy
import requests
import itertools

class SFIA_Skill:
    def __init__(self, name, symbol, definition):
        self.name = name
        self.symbol = symbol
        self.definition = definition

# SFIA skills
sfia_skills = [
    SFIA_Skill("Acceptance testing", "BPTS", "Validating systems, products, business processes or services to determine whether the acceptance criteria have been satisfied."),
    SFIA_Skill("Animation development", "ADEV", "Designing and developing animated and interactive systems such as games and simulations."),
    SFIA_Skill("Application support", "ASUP", "Delivering management, technical and administrative services to support and maintain live applications."),
    SFIA_Skill("Asset management", "ASMG", "Managing the full life cycle of assets from acquisition, operation, maintenance to disposal."),
    SFIA_Skill("Audit", "AUDT", "Delivering independent, risk-based assessments of the effectiveness of processes, the controls, and the compliance environment of an organisation."),
    SFIA_Skill("Availability management", "AVMT", "Ensuring that services deliver agreed levels of availability to meet the current and future needs of the business."),
    SFIA_Skill("Benefits management", "BENM", "Forecasting, planning and monitoring the emergence and effective realisation of anticipated benefits from projects and programmes."),
    SFIA_Skill("Business administration", "ADMN", "Managing and performing administrative services and tasks to enable individuals, teams and organisations to succeed in their objectives."),
    SFIA_Skill("Business intelligence", "BINT", "Developing, producing and delivering regular and one-off management information to provide insights and aid decision-making."),
    SFIA_Skill("Business modelling", "BSMO", "Producing abstract or distilled representations of real-world, business or gaming situations."),
    SFIA_Skill("Business process improvement", "BPRE", "Creating new and potentially disruptive approaches to performing business activities."),
    SFIA_Skill("Business situation analysis", "BUSA", "Investigating business situations to define recommendations for improvement action."),
    SFIA_Skill("Capacity management", "CPMG", "Ensuring that service components have the capacity and performance to meet current and planned business needs."),
    SFIA_Skill("Certification scheme operation", "CSOP", "Designing, developing and operating certification schemes, accreditations and credentials, including digital credentials or badges."),
    SFIA_Skill("Change control", "CHMG", "Assessing risks associated with proposed changes and ensuring changes to products, services or systems are controlled and coordinated."),
    SFIA_Skill("Competency assessment", "LEDA", "Assessing knowledge, skills, competency and behaviours by any means, whether formal or informal, against frameworks such as SFIA."),
    SFIA_Skill("Configuration management", "CFMG", "Planning, identifying, controlling, accounting for and auditing of configuration items (CIs) and their interrelationships."),
    SFIA_Skill("Consultancy", "CNSL", "Providing advice and recommendations, based on expertise and experience, to address client needs."),
    SFIA_Skill("Content authoring", "INCA", "Planning, designing and creating textual information, supported where necessary by graphical content."),
    SFIA_Skill("Content publishing", "ICPM", "Managing and continually improving the processes that collect, assemble and publish content."),
    SFIA_Skill("Continuity management", "COPL", "Developing, implementing and testing a business continuity framework."),
    SFIA_Skill("Contract management", "ITCM", "Managing and controlling the operation of formal contracts for the supply of products and services."),
    SFIA_Skill("Customer service support", "CSMG", "Managing and operating customer service or service desk functions."),
    SFIA_Skill("Data engineering", "DENG", "Designing, building, operationalising, securing and monitoring data pipelines and data stores."),
    SFIA_Skill("Data management", "DATM", "Developing and implementing plans, policies, and practices that control, protect and optimise the value of data assets."),
    SFIA_Skill("Data modelling and design", "DTAN", "Developing models and diagrams to represent and communicate data requirements and data assets."),
    SFIA_Skill("Data science", "DATS", "Applying mathematics, statistics, data mining and predictive modelling techniques to gain insights, predict behaviours and generate value from data."),
    SFIA_Skill("Data visualisation", "VISL", "Facilitating understanding of data by displaying concepts, ideas, and facts using graphical representations."),
    SFIA_Skill("Database administration", "DBAD", "Installing, configuring, monitoring, maintaining and improving the performance of databases and data stores."),
    SFIA_Skill("Database design", "DBDS", "Specifying, designing and maintaining mechanisms for storing and accessing data."),
    SFIA_Skill("Demand management", "DEMM", "Analysing and proactively managing business demand for new services or modifications to existing service features or volumes."),
    SFIA_Skill("Digital forensics", "DGFS", "Recovering and investigating material found in digital devices."),
    SFIA_Skill("Emerging technology monitoring", "EMRG", "Identifying and assessing new and emerging technologies, products, services, methods and techniques."),
    SFIA_Skill("Employee experience", "EEXP", "Enhancing employee engagement and ways of working, empowering employees and supporting their health and wellbeing."),
    SFIA_Skill("Enterprise and business architecture", "STPL", "Aligning an organisation's technology strategy with its business mission, strategy, and processes and documenting this using architectural models."),
    SFIA_Skill("Facilities management", "DCMA", "Planning, designing and managing the buildings, space and facilities which, collectively, make up the IT estate."),
    SFIA_Skill("Feasibility assessment", "FEAS", "Defining, evaluating and describing business change options for financial, technical and business feasibility, and strategic alignment."),
    SFIA_Skill("Financial management", "FMIT", "Supporting the effective use and control of financial resources."),
    SFIA_Skill("Governance", "GOVN", "Defining and operating a framework for making decisions, managing stakeholder relationships, and identifying legitimate authority."),
    SFIA_Skill("Hardware design", "HWDE", "Specifying a hardware design model for a defined system architecture."),
    SFIA_Skill("High-performance computing", "HPCC", "Using advanced computer systems and special programming techniques to solve complex computational problems."),
    SFIA_Skill("Incident management", "USUP", "Coordinating responses to incident reports, minimising negative impacts and restoring service as quickly as possible."),
    SFIA_Skill("Information assurance", "INAS", "Protecting against and managing risks related to the use, storage and transmission of data and information systems."),
    SFIA_Skill("Information management", "IRMG", "Planning, implementing and controlling the full life cycle management of digitally organised information and records."),
    SFIA_Skill("Information security", "SCTY", "Defining and operating a framework of security controls and security management strategies."),
    SFIA_Skill("Information systems coordination", "ISCO", "Coordinating information and technology strategies where the adoption of a common approach would benefit the organisation."),
    SFIA_Skill("Innovation", "INOV", "Identifying, prioritising, incubating and exploiting opportunities provided by information, communication and digital technologies."),
    SFIA_Skill("Investment appraisal", "INVA", "Assessing the attractiveness of possible investments or projects."),
    SFIA_Skill("IT infrastructure", "ITOP", "Deploying, configuring and operating IT Infrastructure."),
    SFIA_Skill("Knowledge management", "KNOW", "Managing vital knowledge to create value for the organisation."),
    SFIA_Skill("Learning and development management", "ETMG", "Delivering management, advisory and administrative services to support the development of knowledge, skills and competencies."),
    SFIA_Skill("Learning delivery", "ETDL", "Transferring knowledge, developing skills and changing behaviours using a range of techniques, resources and media."),
    SFIA_Skill("Learning design and development", "TMCR", "Designing and developing resources to transfer knowledge, develop skills and change behaviours."),
    SFIA_Skill("Machine learning", "MLNG", "Developing systems that learn through experience and by the use of data."),
    SFIA_Skill("Marketing", "MKTG", "Researching, analysing and stimulating potential or existing markets for products and services."),
    SFIA_Skill("Measurement", "MEAS", "Developing and operating a measurement capability to support agreed organisational information needs."),
    SFIA_Skill("Methods and tools", "METL", "Ensuring methods and tools are adopted and used effectively throughout the organisation."),
    SFIA_Skill("Network design", "NTDS", "Designing communication networks to support strategic and operational requirements and producing network strategies, architectures, policies and related documentation."),
    SFIA_Skill("Network support", "NTAS", "Providing maintenance and support services for communications networks."),
    SFIA_Skill("Numerical analysis", "NUAN", "Creating, analysing, implementing, testing and improving algorithms for numerically solving mathematical problems."),
    SFIA_Skill("Organisation design and implementation", "ORDI", "Planning, designing and implementing an integrated organisation structure and culture."),
    SFIA_Skill("Organisational capability development", "OCDV", "Providing leadership, advice and implementation support to assess organisational capabilities and to identify, prioritise and implement improvements."),
    SFIA_Skill("Organisational change management", "CIPM", "Planning, designing and implementing activities to transition the organisation and people to the required future state."),
    SFIA_Skill("Organisational facilitation", "OFCL", "Supporting workgroups to implement principles and practices for effective teamwork across organisational boundaries and professional specialisms."),
    SFIA_Skill("Penetration testing", "PENT", "Testing the effectiveness of security controls by emulating the tools and techniques of likely attackers."),
    SFIA_Skill("Performance management", "PEMT", "Improving organisational performance by developing the performance of individuals and workgroups to meet agreed objectives with measurable results."),
    SFIA_Skill("Personal data protection", "PEDP", "Implementing and operating a framework of controls and management strategies to promote compliance with personal data legislation."),
    SFIA_Skill("Portfolio management", "POMG", "Developing and applying a management framework to define and deliver a portfolio of programmes, projects and/or ongoing services."),
    SFIA_Skill("Portfolio, programme and project support", "PROF", "Providing support and guidance on portfolio, programme and project management processes, procedures, tools and techniques."),
    SFIA_Skill("Problem management", "PBMG", "Managing the life cycle of all problems that have occurred or could occur in delivering a service."),
    SFIA_Skill("Product management", "PROD", "Managing and developing products or services through their full life cycle from inception, growth, maturity, decline to retirement."),
    SFIA_Skill("Professional development", "PDSV", "Facilitating the professional development of individuals in line with their career goals and organisational requirements."),
    SFIA_Skill("Programme management", "PGMG", "Identifying, planning and coordinating a set of related projects and activities in support of specific business strategies and objectives."),
    SFIA_Skill("Programming/software development", "PROG", "Developing software components to deliver value to stakeholders."),
    SFIA_Skill("Project management", "PRMG", "Delivering agreed outcomes from projects using appropriate management techniques, collaboration, leadership and governance."),
    SFIA_Skill("Quality assurance", "QUAS", "Assuring, through ongoing and periodic assessments and reviews, that the organisation’s quality objectives are being met."),
    SFIA_Skill("Quality management", "QUMG", "Defining and operating a management framework of processes and working practices to deliver the organisation's quality objectives."),
    SFIA_Skill("Radio frequency engineering", "RFEN", "Designing, installing and maintaining radio frequency based devices and software."),
    SFIA_Skill("Real-time/embedded systems development", "RESD", "Designing and developing reliable real-time software typically within embedded systems."),
    SFIA_Skill("Release and deployment", "RELM", "Applying the processes, systems and functions required to make new and changed services and features available for use."),
    SFIA_Skill("Requirements definition and management", "REQM", "Managing requirements through the entire delivery and operational life cycle."),
    SFIA_Skill("Research", "RSCH", "Systematically creating new knowledge by data gathering, innovation, experimentation, evaluation and dissemination."),
    SFIA_Skill("Resourcing", "RESC", "Acquiring, deploying and onboarding resources."),
    SFIA_Skill("Risk management", "BURM", "Planning and implementing organisation-wide processes and procedures for the management of risk to the success or integrity of the enterprise."),
    SFIA_Skill("Safety assessment", "SFAS", "Assessing safety-related software and hardware systems to determine compliance with standards and required levels of safety integrity."),
    SFIA_Skill("Safety engineering", "SFEN", "Applying appropriate methods to assure safety during all life cycle phases of safety-related systems developments."),
    SFIA_Skill("Sales support", "SSUP", "Providing advice and support to the sales force, customers and sales partners."),
    SFIA_Skill("Scientific modelling", "SCMO", "Applying computer simulation and other forms of computation to solve real-world problems in scientific disciplines."),
    SFIA_Skill("Security operations", "SCAD", "Delivering management, technical and administrative services to implement security controls and security management strategies."),
    SFIA_Skill("Selling", "SALE", "Finding prospective customers and working with them to identify needs, influence purchase decisions and enhance future business opportunities."),
    SFIA_Skill("Service acceptance", "SEAC", "Managing the process to obtain formal confirmation that service acceptance criteria have been met."),
    SFIA_Skill("Service catalogue management", "SCMG", "Providing a source of consistent information about available services and products to customers and users."),
    SFIA_Skill("Service level management", "SLMO", "Agreeing targets for service levels and assessing, monitoring, and managing the delivery of services against the targets."),
    SFIA_Skill("Software configuration", "PORT", "Designing and deploying software product configurations into software environments or platforms."),
    SFIA_Skill("Software design", "SWDN", "Specifying and designing software to meet defined requirements by following agreed design standards and principles."),
    SFIA_Skill("Solution architecture", "ARCH", "Developing and communicating a multi-dimensional solution architecture to deliver agreed business outcomes."),
    SFIA_Skill("Sourcing", "SORC", "Managing, or providing advice on, the procurement or commissioning of products and services."),
    SFIA_Skill("Specialist advice", "TECH", "Providing authoritative advice and direction in a specialist area."),
    SFIA_Skill("Stakeholder relationship management", "RLMT", "Influencing stakeholder attitudes, decisions, and actions for mutual benefit."),
    SFIA_Skill("Storage management", "STMG", "Planning, implementing and optimising the technologies and processes used for data storage."),
    SFIA_Skill("Strategic planning", "ITSP", "Creating and maintaining a strategy to align organisational actions, plans and resources with business objectives."),
    SFIA_Skill("Subject formation", "SUBF", "Specifying, designing and developing curricula within a structured and systematic education environment."),
    SFIA_Skill("Supplier management", "SUPP", "Aligning the organisation's supplier performance objectives and activities with sourcing strategies and plans, balancing costs, efficiencies and service quality."),
    SFIA_Skill("Sustainability", "SUST", "Providing advice, assistance and leadership to enable the organisation to minimise negative environmental impact."),
    SFIA_Skill("System software", "SYSP", "Installing, managing, controlling, deploying and maintaining infrastructure systems software, to meet operational needs and service levels."),
    SFIA_Skill("Systems and software life cycle engineering", "SLEN", "Establishing and deploying an environment for developing, continually improving, and securely operating software and systems products and services."),
    SFIA_Skill("Systems design", "DESN", "Designing systems to meet specified requirements and agreed systems architectures."),
    SFIA_Skill("Systems development management", "DLMG", "Planning, estimating and executing systems development work to time, budget and quality targets."),
    SFIA_Skill("Systems installation and removal", "HSIN", "Installing and testing, or decommissioning and removing, systems or system components."),
    SFIA_Skill("Systems integration and build", "SINT", "Planning, implementing and controlling activities to synthesise system components to create operational systems, products or services."),
    SFIA_Skill("Teaching", "TEAC", "Delivering and assessing curricula in a structured and systematic education environment."),
    SFIA_Skill("Technology service management", "ITMG", "Managing the provision of technology-based services to meet defined organisational needs."),
    SFIA_Skill("Testing", "TEST", "Investigating products, systems and services to assess behaviour and whether this meets specified or unspecified requirements and characteristics."),
    SFIA_Skill("Threat intelligence", "THIN", "Developing and sharing actionable insights on current and potential security threats to the success or integrity of an organisation."),
    SFIA_Skill("User experience analysis", "UNAN", "Understanding the context of use for systems, products and services and specifying user experience requirements and design goals."),
    SFIA_Skill("User experience design", "HCEV", "Producing design concepts and prototypes for user interactions with and experiences of a product, system or service."),
    SFIA_Skill("User experience evaluation", "USEV", "Validating systems, products or services against user experience goals, metrics and targets."),
    SFIA_Skill("User research", "URCH", "Identifying users' behaviours, needs and motivations using observational research methods."),
    SFIA_Skill("Vulnerability assessment", "VUAS", "Identifying and classifying security vulnerabilities in networks, systems and applications and mitigating or eliminating their impact."),
    SFIA_Skill("Vulnerability research", "VURE", "Conducting applied research to discover, evaluate and mitigate new or unknown security vulnerabilities and weaknesses."),
    SFIA_Skill("Workforce planning", "WFPL", "Estimating the demand for people and skills and planning the supply needed to meet that demand.")
]

# URL of the server
url = 'http://localhost:8081/upload'

# Path to the resume file
resume_file_path = '/home/brandontrainee/repos/training/CS50x_2024/project/training_data/resumes/Brandon_Maruna_Resume_2023(v2).docx'

# Set up the request headers
headers = {}

# Create a dictionary containing the file to be uploaded
files = {'resume': open(resume_file_path, 'rb')}

# Make the HTTP POST request to the server
response = requests.post(url, files=files, headers=headers)

skills = ''
education_training = ''

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    parsed_data = response.json()
    
    # Extract the skills section from the response
    skills_data = parsed_data.get('data', {}).get('skills', [])
    summary_data = parsed_data.get('data', {}).get('summary', [])
    
    # Extract text from dictionaries in skills_data and education_training_data
    skills_text = ' '.join(skill.get('KEY SKILLS', '') for skill in skills_data)
    summary_text = ' '.join(summary.get('PROFILE', '') for summary in summary_data)
    
    # Process the skills and education_training texts with spaCy
    nlp = spacy.load('en_core_web_md')
    resumeSkills = nlp(skills_text)
    summarySkills = nlp(summary_text)
    
    # Function to check similarity between a sentence and SFIA skill definition
    def get_similarity(sentence, sfia_skill):
        doc1 = nlp(sentence)
        doc2 = nlp(sfia_skill.definition)
        return doc1.similarity(doc2)

    # Print out the sentences from the skills and education/training sections
    for sentence in itertools.chain(resumeSkills.sents, summarySkills.sents):
        if len(sentence.text.split()) < 5:
            continue
        for sfia_skill in sfia_skills:
            similarity = get_similarity(sentence.text, sfia_skill)

            if similarity > 0.905:
                print(f"Match found: '{sfia_skill.name}' with similarity {similarity}")

else:
    # Print out the error response
    print("Error:", response.status_code)
    print("Error Response:", response.text)
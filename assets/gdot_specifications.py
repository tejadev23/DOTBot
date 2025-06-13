# GDOT Specifications Data Extracted from 2021 Standard Specifications
# This dictionary contains sections 101, 102, 103, 104, 109, 110, 148, 149, 150, 151, and 152
# Structure: {section_number: {title, page, subsections, tables}}
# Subsections: {subsection_number: {title, content, page, tables (if any)}}
# Tables: List of dictionaries representing rows
# Page numbers start at 1 for the split document, incrementing per section
# Intended for integration into a chatbot model handling multiple data sources

gdot_specifications = {
    "101": {
        "title": "Definition and Terms",
        "page": "1",
        "subsections": {
            "101.01": {
                "title": "Abbreviations",
                "content": "Defines abbreviations used in Specifications or Plans.",
                "page": "1",
                "tables": [
                    [
                        {"Abbreviation": "AAN", "Term": "American Association of Nurserymen"},
                        {"Abbreviation": "AAR", "Term": "Association of American Railroads"},
                        {"Abbreviation": "AASHTO", "Term": "American Association of State Highway and Transportation Officials"},
                        {"Abbreviation": "ACI", "Term": "American Concrete Institute"},
                        {"Abbreviation": "AGC", "Term": "Associated General Contractors of America"},
                        {"Abbreviation": "AIA", "Term": "American Institute of Architects"},
                        {"Abbreviation": "AIEE", "Term": "American Institute of Electrical Engineers"},
                        {"Abbreviation": "AISC", "Term": "American Institute of Steel Construction"},
                        {"Abbreviation": "AISI", "Term": "American Iron and Steel Institute"},
                        {"Abbreviation": "AMS", "Term": "Aerospace Materials Specification"},
                        {"Abbreviation": "ANSI", "Term": "American National Standards Institute"},
                        {"Abbreviation": "ARA", "Term": "American Railway Association"},
                        {"Abbreviation": "AREA", "Term": "American Railway Engineering Association"},
                        {"Abbreviation": "ASCE", "Term": "American Society of Civil Engineers"},
                        {"Abbreviation": "ASLA", "Term": "American Society of Landscape Architects"},
                        {"Abbreviation": "ASTM", "Term": "American Society of Testing and Materials"},
                        {"Abbreviation": "AWPA", "Term": "American Wood Preservers' Association"},
                        {"Abbreviation": "AWWA", "Term": "American Water Works Association"},
                        {"Abbreviation": "AWS", "Term": "American Welding Society"},
                        {"Abbreviation": "CRSI", "Term": "Concrete Reinforcing Steel Institute"},
                        {"Abbreviation": "DOT", "Term": "Georgia Department of Transportation"},
                        {"Abbreviation": "EEO", "Term": "Equal Employment Opportunity"},
                        {"Abbreviation": "FHWA", "Term": "Federal Highway Administration"},
                        {"Abbreviation": "FSS", "Term": "Federal Specifications and Standards, General Services Administration"},
                        {"Abbreviation": "GDT", "Term": "Georgia Department of Transportation"},
                        {"Abbreviation": "IES", "Term": "Illuminating Engineering Society"}
                    ],
                    [
                        {"Abbreviation": "MUTCD", "Term": "Manual on Uniform Traffic Control Devices"},
                        {"Abbreviation": "NEC", "Term": "National Electrical Code"},
                        {"Abbreviation": "NEMA", "Term": "National Electrical Manufacturers Association"},
                        {"Abbreviation": "NESC", "Term": "National Electrical Safety Code"},
                        {"Abbreviation": "NFPA", "Term": "National Fire Protection Association"},
                        {"Abbreviation": "SAE", "Term": "Society of Automotive Engineers"},
                        {"Abbreviation": "SPIB", "Term": "Southern Pine Inspection Bureau"},
                        {"Abbreviation": "SSPC", "Term": "Steel Structure Painting Council"},
                        {"Abbreviation": "UL", "Term": "Underwriters Laboratories, Inc."}
                    ]
                ]
            },
            "101.02": {
                "title": "Acceptance Plans",
                "content": "Method for evaluating measurements to determine acceptability of material or construction.",
                "page": "1"
            },
            "101.03": {
                "title": "Advertisement",
                "content": "Public announcement inviting bids for work or materials.",
                "page": "1"
            },
            "101.04": {
                "title": "Available Day",
                "content": "Calendar day (excluding weekends/holidays) where at least five hours of productive work is possible, unless prevented by uncontrollable causes.",
                "page": "1"
            },
            "101.05": {
                "title": "Award",
                "content": "Formal acceptance of a Bid by the Department.",
                "page": "1"
            },
            "101.06": {
                "title": "Base Course",
                "content": "Layers of material on subgrade/subbase to support surface course.",
                "page": "1"
            },
            "101.07": {
                "title": "Bid",
                "content": "See Proposal.",
                "page": "1"
            },
            "101.08": {
                "title": "Bid Item",
                "content": "Described unit of work with a requested price in the proposal.",
                "page": "1"
            },
            "101.09": {
                "title": "Bidder",
                "content": "Qualified entity submitting a Proposal.",
                "page": "1"
            },
            "101.10": {
                "title": "Board",
                "content": "State Transportation Board for GDOT.",
                "page": "1"
            },
            "101.11": {
                "title": "Bridge",
                "content": "Structure over 20 ft. (6 m) for traffic or loads, including substructure and superstructure. Subterms: Bridge Length, Bridge Roadway Width, Bridge Complete, Completed Bridge Site.",
                "page": "1"
            },
            "101.12": {
                "title": "Calendar Day",
                "content": "Every day starting at midnight.",
                "page": "1"
            },
            "101.13": {
                "title": "Chief Engineer",
                "content": "Engineering Executive appointed by the State Transportation Board.",
                "page": "1"
            },
            "101.14": {
                "title": "Commissioner",
                "content": "Commissioner of GDOT.",
                "page": "1"
            },
            "101.15": {
                "title": "Completion Date",
                "content": "Calendar date for Contract completion if specified in Proposal.",
                "page": "1"
            },
            "101.16": {
                "title": "Contract",
                "content": "Written agreement including Advertisement, Proposal, Contract Form, Bond, Specifications, Plans, etc.",
                "page": "1"
            },
            "101.17": {
                "title": "Contract Bond (Performance and Payment Bond)",
                "content": "Security guaranteeing Contract execution and payment of debts.",
                "page": "1"
            },
            "101.18": {
                "title": "Contract Item (Pay Item)",
                "content": "Unit of work with a price in the Contract.",
                "page": "1"
            },
            "101.19": {
                "title": "Contract Time",
                "content": "Number of available or calendar days for Contract completion.",
                "page": "1"
            },
            "101.20": {
                "title": "Contractor",
                "content": "Entity contracting with GDOT for work.",
                "page": "1"
            },
            "101.21": {
                "title": "Culvert",
                "content": "Structure under roadway with opening ≤ 20 ft. (6 m).",
                "page": "1"
            },
            "101.22": {
                "title": "Department",
                "content": "Georgia Department of Transportation.",
                "page": "1"
            },
            "101.23": {
                "title": "Easement",
                "content": "Right to use/control property for a purpose without title.",
                "page": "1"
            },
            "101.24": {
                "title": "Engineer",
                "content": "Chief Engineer or authorized representative.",
                "page": "1"
            },
            "101.25": {
                "title": "Equipment",
                "content": "Machinery, tools, and supplies for construction.",
                "page": "1"
            },
            "101.26": {
                "title": "Extension Agreement",
                "content": "Agreement extending work beyond original boundaries.",
                "page": "1"
            },
            "101.27": {
                "title": "Extra Work",
                "content": "Essential work not in original Contract.",
                "page": "1"
            },
            "101.28": {
                "title": "Force Account",
                "content": "Payment method for Extra Work without Supplemental Agreement.",
                "page": "1"
            },
            "101.29": {
                "title": "General Terms",
                "content": "Terms implying Engineer's authority unless context differs.",
                "page": "1"
            },
            "101.30": {
                "title": "Highway—Road—Street",
                "content": "Public way for vehicular travel within Rights of Way.",
                "page": "1"
            },
            "101.31": {
                "title": "Holidays",
                "content": "State holidays with specific dates or rules for weekends.",
                "page": "2",
                "tables": [
                    [
                        {"Date": "January 1", "Holiday": "New Year's Day"},
                        {"Date": "3rd Monday in January", "Holiday": "King's Birthday"},
                        {"Date": "January 19", "Holiday": "State Holiday"},
                        {"Date": "3rd Monday in February", "Holiday": "Washington's Birthday"},
                        {"Date": "April 26", "Holiday": "State Holiday"},
                        {"Date": "Last Monday in May", "Holiday": "National Memorial Day"},
                        {"Date": "July 4", "Holiday": "Independence Day"},
                        {"Date": "1st Monday in September", "Holiday": "Labor Day"},
                        {"Date": "2nd Monday in October", "Holiday": "Columbus Day"},
                        {"Date": "November 11", "Holiday": "Veterans' Day"},
                        {"Date": "4th Thursday in November", "Holiday": "Thanksgiving Day"},
                        {"Date": "December 25", "Holiday": "Christmas Day"}
                    ]
                ]
            },
            "101.32": {
                "title": "Inspector",
                "content": "Engineer's representative for detailed inspection.",
                "page": "2"
            },
            "101.33": {
                "title": "Invitation for Bids",
                "content": "See Advertisement.",
                "page": "2"
            },
            "101.34": {
                "title": "Laboratory",
                "content": "GDOT or designated testing laboratory.",
                "page": "2"
            },
            "101.35": {
                "title": "Liquidated Damages",
                "content": "Charges for failure to complete Contract on time.",
                "page": "2"
            },
            "101.36": {
                "title": "Materials",
                "content": "Substances for construction.",
                "page": "2"
            },
            "101.37": {
                "title": "Materials Allowance",
                "content": "Payment for materials on hand per Subsection 109.07.",
                "page": "2"
            },
            "101.38": {
                "title": "Median",
                "content": "Portion of divided highway separating opposite traffic.",
                "page": "2"
            },
            "101.39": {
                "title": "Minor Structures",
                "content": "Structures not defined as bridges.",
                "page": "2"
            },
            "101.40": {
                "title": "Notice to Contractors",
                "content": "Notice soliciting Proposals with work/material details.",
                "page": "2"
            },
            "101.41": {
                "title": "Notice to Proceed",
                "content": "Written notice to start Contract work.",
                "page": "2"
            },
            "101.42": {
                "title": "Pavement Structure",
                "content": "Subbase, base course, and surface course on subgrade.",
                "page": "2"
            },
            "101.43": {
                "title": "Pay Item",
                "content": "See Contract Item.",
                "page": "2"
            },
            "101.44": {
                "title": "Performance and Payment Bond",
                "content": "See Contract Bond.",
                "page": "2"
            },
            "101.45": {
                "title": "Plans",
                "content": "Approved drawings showing work details.",
                "page": "2"
            },
            "101.46": {
                "title": "Prequalification",
                "content": "Procedure to establish Bidder responsibility.",
                "page": "2"
            },
            "101.47": {
                "title": "Project",
                "content": "Transportation system section under Contract.",
                "page": "2"
            },
            "101.48": {
                "title": "Proposal",
                "content": "Bidder’s offer to perform work at quoted prices.",
                "page": "2"
            },
            "101.49": {
                "title": "Proposal Guaranty",
                "content": "Surety ensuring Bidder enters Contract if awarded.",
                "page": "2"
            },
            "101.50": {
                "title": "Right-of-Way",
                "content": "Land acquired for highway and structures.",
                "page": "2"
            },
            "101.51": {
                "title": "Roadbed",
                "content": "Graded highway portion for pavement and shoulder.",
                "page": "2"
            },
            "101.52": {
                "title": "Roadside Development",
                "content": "Items for landscape preservation, erosion control, and aesthetics.",
                "page": "2"
            },
            "101.53": {
                "title": "Roadway",
                "content": "Highway portion within construction limits.",
                "page": "2"
            },
            "101.54": {
                "title": "Salvaged Material",
                "content": "Valuable material to be preserved or reused.",
                "page": "2"
            },
            "101.55": {
                "title": "Shall or Will, Should, May",
                "content": "Shall/Will: Mandatory; Should: Advisory; May: Permissive.",
                "page": "2"
            },
            "101.56": {
                "title": "Shoulder",
                "content": "Roadway portion for stopped vehicles and support.",
                "page": "2"
            },
            "101.57": {
                "title": "Sidewalk",
                "content": "Roadway portion for pedestrians.",
                "page": "2"
            },
            "101.58": {
                "title": "Skew or Skew Angle",
                "content": "Acute angle between roadway and bridge/culvert elements.",
                "page": "2"
            },
            "101.59": {
                "title": "Special Provisions",
                "content": "Additions/revisions to Specifications, general or project-specific.",
                "page": "2"
            },
            "101.60": {
                "title": "Specifications",
                "content": "Directions, provisions, and requirements for work.",
                "page": "2"
            },
            "101.61": {
                "title": "Standard Specifications",
                "content": "GDOT publication for transportation systems construction.",
                "page": "2"
            },
            "101.62": {
                "title": "State Highway Engineer",
                "content": "See Chief Engineer.",
                "page": "2"
            },
            "101.63": {
                "title": "State",
                "content": "State of Georgia.",
                "page": "2"
            },
            "101.64": {
                "title": "Station",
                "content": "100 linear ft. (1 km) measured horizontally.",
                "page": "2"
            },
            "101.65": {
                "title": "Structures",
                "content": "Bridges, culverts, walls, sewers, etc.",
                "page": "2"
            },
            "101.66": {
                "title": "Subbase",
                "content": "Layer on subgrade to support base course.",
                "page": "2"
            },
            "101.67": {
                "title": "Subcontractor",
                "content": "Entity sublet part of Contract with GDOT consent.",
                "page": "2"
            },
            "101.68": {
                "title": "Subgrade",
                "content": "Top 12 in. (300 mm) of roadbed for pavement.",
                "page": "2"
            },
            "101.69": {
                "title": "Subgrade Treatment",
                "content": "Stabilization of subgrade material.",
                "page": "2"
            },
            "101.70": {
                "title": "Stabilization",
                "content": "Soil/aggregate modification for strength.",
                "page": "2"
            },
            "101.71": {
                "title": "Substructure",
                "content": "Bridge portion below bearings or footings.",
                "page": "2"
            },
            "101.72": {
                "title": "Superintendent",
                "content": "Contractor’s representative for work supervision.",
                "page": "2"
            },
            "101.73": {
                "title": "Superstructure",
                "content": "Bridge portion except substructure.",
                "page": "2"
            },
            "101.74": {
                "title": "Supplemental Agreement",
                "content": "Agreement modifying Contract terms.",
                "page": "2"
            },
            "101.75": {
                "title": "Supplemental Specifications",
                "content": "Approved additions/revisions to Standard Specifications.",
                "page": "2"
            },
            "101.76": {
                "title": "Surety",
                "content": "Entity executing Bond for Contractor.",
                "page": "2"
            },
            "101.77": {
                "title": "The Work",
                "content": "All labor, materials, and incidentals for Project completion.",
                "page": "2"
            },
            "101.78": {
                "title": "Titles (or Headings)",
                "content": "For reference, not affecting interpretation.",
                "page": "2"
            },
            "101.79": {
                "title": "Traveled Way",
                "content": "Roadway for vehicle movement, excluding shoulders.",
                "page": "2"
            },
            "101.80": {
                "title": "Treasurer",
                "content": "Treasurer of GDOT.",
                "page": "2"
            },
            "101.81": {
                "title": "Working Drawings",
                "content": "Contractor-submitted drawings for approval.",
                "page": "2"
            },
            "101.82": {
                "title": "Related References",
                "content": "Listed for convenience, not affecting interpretation.",
                "page": "2"
            }
        },
        "tables": []
    },
    "102": {
        "title": "Bidding Requirements and Conditions",
        "page": "3",
        "subsections": {
            "102.01": {
                "title": "Prequalification of Bidders",
                "content": "Bids > $2,000,000 require prequalification; ≤ $2,000,000 require registration. Aggregate contract amount limited by Bidder’s Current Capacity.",
                "page": "3"
            },
            "102.02": {
                "title": "Competency of Bidders",
                "content": "Department may limit work based on prequalification or performance issues.",
                "page": "3"
            },
            "102.03": {
                "title": "Contents of Proposal Forms",
                "content": "Proposal Form includes project details, quantities, completion time, guaranty, and Special Provisions.",
                "page": "3"
            },
            "102.04": {
                "title": "Interpretation of Estimates",
                "content": "Quantities are approximate; payment based on actual work performed.",
                "page": "3"
            },
            "102.05": {
                "title": "Examination of Plans, Specifications, Special Provisions, and Site of the Work",
                "content": "Bidders must examine site and documents; submission implies satisfaction with conditions.",
                "page": "3"
            },
            "102.06": {
                "title": "Preparation of Proposal",
                "content": "Proposals submitted via GDOT form, with Unit Prices, Non-Collusion Certificate, and other required forms. Electronic submission via AASHTOWare Project Bids required.",
                "page": "3"
            },
            "102.07": {
                "title": "Rejection of Proposals",
                "content": "Proposals may be rejected for conditional bids, non-compliance, collusion, unbalanced bids, or other irregularities.",
                "page": "3"
            },
            "102.08": {
                "title": "Proposal Guaranty",
                "content": "Required surety for each bid, specific to the Proposal.",
                "page": "3"
            },
            "102.09": {
                "title": "Delivery of Proposals",
                "content": "Proposals submitted sealed or electronically via Bid Express by deadline.",
                "page": "3"
            },
            "102.10": {
                "title": "Withdrawal or Revision of Proposals",
                "content": "Bidders may withdraw/revise via Bid Express before deadline.",
                "page": "3"
            },
            "102.11": {
                "title": "Public Bid",
                "content": "Bid results posted on Bid Express and GDOT website.",
                "page": "3"
            },
            "102.12": {
                "title": "Material Guaranty",
                "content": "Department may require material origin and quality statements.",
                "page": "3"
            },
            "102.13": {
                "title": "Combination or Conditional Proposals",
                "content": "Department may issue combined/separate bids; conditional bids only if specified.",
                "page": "3"
            },
            "102.14": {
                "title": "Landscape Projects",
                "content": "Requires qualified Landscape Contractors with certified nursery stock and licenses.",
                "page": "3"
            },
            "102.15": {
                "title": "Submittal of 'Georgia Security and Immigration Compliance Act Affidavit'",
                "content": "Required by low Bidder post-bid opening.",
                "page": "3"
            },
            "102.16": {
                "title": "Submittal of 'Request For Eligibility To Bid'",
                "content": "Required by all Bidders pre-bid opening.",
                "page": "3"
            },
            "102.17": {
                "title": "Submittal of 'Certificate of Current Capacity' and 'Status of Contracts on Hand'",
                "content": "Required by low Bidder post-bid opening.",
                "page": "3"
            },
            "102.18": {
                "title": "Submittal of 'Construction Contractors Bid Opportunity List'",
                "content": "Required by all Bidders post-bid opening.",
                "page": "3"
            },
            "102.19": {
                "title": "Specialty Items Exempt from Prequalification of Bidders",
                "content": "Utility work approved by owner exempt from prequalification.",
                "page": "3"
            }
        },
        "tables": []
    },
    "103": {
        "title": "Award and Execution of Contract",
        "page": "4",
        "subsections": {
            "103.01": {
                "title": "Consideration of Proposals",
                "content": "Bids compared based on Unit Prices; Department may reject or waive technicalities.",
                "page": "4"
            },
            "103.02": {
                "title": "Award of Contract",
                "content": "Awarded to lowest reliable Bidder within 50 days, subject to federal concurrence.",
                "page": "4"
            },
            "103.03": {
                "title": "Cancellation of Award",
                "content": "Department may cancel Award before execution without liability.",
                "page": "4"
            },
            "103.04": {
                "title": "Return of Proposal Guaranty",
                "content": "Reserved.",
                "page": "4"
            },
            "103.05": {
                "title": "Requirements of Contract Bonds",
                "content": "Bonds at 210% of Contract amount; nonresident Contractors require tax bond.",
                "page": "4"
            },
            "103.06": {
                "title": "Execution and Approval of Contract",
                "content": "Bidder signs within 15 days; effective upon full execution.",
                "page": "4"
            },
            "103.07": {
                "title": "Failure to Execute Contract",
                "content": "Failure to sign forfeits Proposal Guaranty; Department may re-award.",
                "page": "4"
            },
            "103.08": {
                "title": "Procedure for Requesting Reconsideration by Responsive Rejected Apparent Low Bidder",
                "content": "Rejected low Bidder may request meeting within 2 days; decision within 3 days post-meeting.",
                "page": "4"
            }
        },
        "tables": []
    },
    "104": {
        "title": "Scope of Work",
        "page": "5",
        "subsections": {
            "104.01": {
                "title": "Intent of Contract",
                "content": "Contractor provides all resources to complete work per Plans and Specifications.",
                "page": "5"
            },
            "104.02": {
                "title": "Special Work",
                "content": "Special Provisions govern if conflicting with Standard Specifications.",
                "page": "5"
            },
            "104.03": {
                "title": "Alteration of Plans or Character of Work",
                "content": """A. Authority to Make Changes:
The Department reserves the right to make, at any time during the progress of the work, such increases or decreases in quantities and such alterations in the details of construction, including alterations in the grade or alignment of the road or structure or both, as may be found necessary or desirable. Such increases or decreases and alterations shall not invalidate the contract nor release the Surety, and the Contractor agrees to perform The Work as altered, the same as if it had been a part of the original Contract.

Whenever an alteration in character of work involves a substantial change in the nature of the design or in the type of construction or materially increases or decreases the cost of performance, a Supplemental Agreement acceptable to both parties shall be executed before work is started on such alteration, except that in the absence of a Supplemental Agreement acceptable to both parties, the Engineer may direct that the work be done by Force Account. Any Force Account Agreement shall be in writing, specifying the terms of payment, signed by the State Construction Engineer and agreed to in writing by the Contractor.

All work shall be performed as directed and in accordance with the Specifications.

B. No Waiver of Contract:
Changes made by the Engineer will not be considered to waive any of the provisions of the Contract, nor may the Contractor make any claim for loss of anticipated profits because of the changes, or by reason of any variation between the approximate quantities and the quantities of work as done.

C. Certain Items Not Limited:
The quantities of all types of excavation, embankment when a Pay Item, perforated underdrain pipe, ditch paving, subgrade treatment materials, stabilizers, extra depth of concrete including its reinforcement, piling, guard rail, asphaltic concrete leveling, erosion control items, traffic control items, slope paving, bridge rip-rap, filter fabric, or any other items that cannot conveniently be determined accurately until after The Work is in progress, and any increase or decrease in these quantities, whatever the amount, will be considered normal overruns or underruns. The Engineer has unlimited authority to increase or decrease these quantities.

D. Changes in Other Quantities:
The Engineer may increase or decrease the quantities of any and all other Pay Items, without changing the Unit Prices Bid, provided that the sum total of such changes, exclusive of changes in those items covered in Subsection 104.03.C, does not increase or decrease the original Contract amount by more than 20 percent.

E. Changes to Original Length or Cost of Project:
The Engineer has the authority to extend or reduce the total length or total cost of the Project by as much as 20 percent. The provisions of Subsection 104.03.C, covering overruns or underruns of certain Pay Items apply also to overruns or underruns in quantities resulting from an extension or reduction in the length of the Project. If the Project is extended in length, an Extension Agreement will be executed. If the Extension Agreement calls for Pay Items already in the Contract, the Unit Prices for such Items will not be changed except as provided in Subsections 104.03.A, 104.03.B and 104.03.D. New work for which no Unit Prices have been Bid will be paid for as Extra Work as defined in Subsection 104.04.

F. Railroad Grade Separation Structures:
Changes in design or construction features of railroad grade separation structures must be submitted to the Engineer of the railroad for approval. The Department will diligently expedite all correspondence with the railroad officials but will not be responsible to the Contractor for any delay to the Contractor’s work resulting from delay in securing the necessary approval. The Engineer will give due consideration to such delays in determining the time for completion of the Contract.""",
                "page": "5"
            },
            "104.04": {
                "title": "Extra Work",
                "content": "Unforeseen work paid per Subsection 109.05.",
                "page": "5"
            },
            "104.05": {
                "title": "Maintenance During Construction",
                "content": "Contractor maintains Project until acceptance, including traffic control and safety features.",
                "page": "5"
            },
            "104.06": {
                "title": "Right in and Use of Materials Found on the Project",
                "content": "Contractor may use approved materials on-site, paid at bid price minus new material cost if reused.",
                "page": "5"
            }
        },
        "tables": []
    },
    "109": {
        "title": "Measurement and Payment",
        "page": "6",
        "subsections": {
            "109.07": {
                "title": "Partial Payments",
                "content": "Monthly payments for completed work and materials on hand, subject to deductions.",
                "page": "6"
            },
            "109.08": {
                "title": "Final Payment",
                "content": "Final Statement prepared post-acceptance; Contractor has 35 days to review. Standard Release Form executed within 45 days.",
                "page": "6"
            },
            "109.09": {
                "title": "Termination Clause",
                "content": "Department may terminate Contract for convenience or specific conditions; payments for completed work and materials.",
                "page": "6"
            },
            "109.10": {
                "title": "Interest",
                "content": "No prejudgment interest on claims; Contractor waives certain statutory rights.",
                "page": "6"
            },
            "109.11": {
                "title": "Price Adjustments",
                "content": "Asphalt cement price adjustments calculated monthly using formulas: PA = [(APM - APL) / APL] × TMT × APL.",
                "page": "6"
            }
        },
        "tables": []
    },
    "110": {
        "title": "Electronic Delivery Management System (e-Ticketing)",
        "page": "7",
        "subsections": {
            "110.1": {
                "title": "General Description",
                "content": "Automated e-Ticketing System for tracking asphalt, concrete, and aggregate deliveries.",
                "page": "7"
            },
            "110.2": {
                "title": "Construction Requirements",
                "content": "Contractor submits e-Ticketing supplier 30 days prior; system tracks vehicles and integrates with scales.",
                "page": "7"
            },
            "110.3": {
                "title": "Measurement",
                "content": "No separate measurement unless specified in Plans.",
                "page": "7"
            },
            "110.4": {
                "title": "Payment",
                "content": "Included in material costs unless listed as separate Item No. 110.",
                "page": "7"
            }
        },
        "tables": []
    },
    "148": {
        "title": "Pilot Vehicles",
        "page": "8",
        "subsections": {
            "148.1": {
                "title": "General Description",
                "content": "Specifications included elsewhere in Contract.",
                "page": "8"
            }
        },
        "tables": []
    },
    "149": {
        "title": "Construction Layout",
        "page": "9",
        "subsections": {
            "149.1": {
                "title": "General Description",
                "content": """Perform construction layout to guide and control performance of items of the work according to this specification. This work includes:
• Placing, replacing (if necessary), and maintaining construction layout points.
• Preparing construction layout drawings, sketches, and computations.
• Recording data in field books such as alignment, slope stake, blue top, drainage layout, bridge, and other books used for layout for this project.""",
                "page": "9"
            },
            "149.2": {
                "title": "Materials",
                "content": "Per General Provisions 101-150.",
                "page": "9"
            },
            "149.3": {
                "title": "Construction Requirements",
                "content": "Verify alignments, elevations, and submit sketches for bridges, walls, and drainage.",
                "page": "9"
            },
            "149.4": {
                "title": "Measurement",
                "content": "Not measured for payment.",
                "page": "9"
            },
            "149.5": {
                "title": "Payment",
                "content": "Included in related work items.",
                "page": "9"
            }
        },
        "tables": []
    },
    "150": {
        "title": "Traffic Control",
        "page": "10",
        "subsections": {
            "150.1": {
                "title": "General Description",
                "content": "Specifications included elsewhere in Contract.",
                "page": "10"
            }
        },
        "tables": []
    },
    "151": {
        "title": "Mobilization",
        "page": "11",
        "subsections": {
            "151.1": {
                "title": "General Description",
                "content": "Preparatory work and operations, including moving resources to site.",
                "page": "11"
            },
            "151.2": {
                "title": "Materials",
                "content": "Per General Provisions 101-150.",
                "page": "11"
            },
            "151.3": {
                "title": "Construction Requirements",
                "content": "Per General Provisions 101-150.",
                "page": "11"
            },
            "151.4": {
                "title": "Measurement",
                "content": "Not measured separately.",
                "page": "11"
            },
            "151.5": {
                "title": "Payment",
                "content": "Partial payments up to 3% of Contract amount; Item No. 151.",
                "page": "11"
            }
        },
        "tables": []
    },
    "152": {
        "title": "Field Laboratory Building",
        "page": "12",
        "subsections": {
            "152.1": {
                "title": "General Description",
                "content": "Furnish and maintain field laboratory for Engineer’s use.",
                "page": "12"
            },
            "152.2": {
                "title": "Materials",
                "content": "Per General Provisions 101-150.",
                "page": "12"
            },
            "152.3": {
                "title": "Construction Requirements",
                "content": "Provide laboratory with specified dimensions, equipment, and facilities.",
                "page": "12"
            },
            "152.4": {
                "title": "Measurement",
                "content": "Measured per laboratory furnished.",
                "page": "12"
            },
            "152.5": {
                "title": "Payment",
                "content": "Paid in two installments; Item No. 152.",
                "page": "12"
            }
        },
        "tables": []
    }
}
from datasets import Dataset
from pprint import pprint

json_data = [
    {
        "conversations": [
            {
                "content": "Can you list some city parks in Flagstaff, Arizona?",
                "role": "user"
            },
            {
                "content": "Certainly! Here are some city parks in Flagstaff, Arizona:\n\n- **Bushmaster Park**: Located at 3150 N Alta Vista Dr, this 20-acre park features playgrounds, lighted tennis and basketball courts, a skate park, roller skating arena, dog park, picnic ramadas, and permanent restrooms.\n\n- **Thorpe Park**: Situated at 191 N Thorpe Rd, Thorpe Park offers playgrounds, lighted tennis courts, sand volleyball court, basketball court, soccer fields, youth baseball fields, adult softball fields, a disc golf course, dog park, picnic ramada, and both portable and permanent restrooms.\n\n- **Foxglenn Park**: Found at 4200 E Butler Ave, this park includes a playground, basketball courts, soccer fields, a youth softball field, skate track, picnic ramadas, and permanent restrooms.\n\n- **Buffalo Park**: Located at 2400 N Gemini Rd, Buffalo Park is a 215-acre open space with a 2-mile loop trail, picnic ramada, and permanent restrooms, offering scenic views and opportunities for walking, running, and wildlife observation.\n\n- **Ponderosa Trails Park**: At 3875 S Wild West Trail, this park features a playground, picnic ramada, portable restrooms, and open grassy areas suitable for various recreational activities.\n\n- **McPherson Park**: Situated at 1650 N Turquoise Dr, McPherson Park offers a playground, tennis courts, basketball court, horseshoe courts, a disc golf course, and portable restrooms.\n\n- **Cheshire Park**: Located at 3000 N Fremont Blvd, this park includes a playground, tennis court, basketball courts, picnic ramada, and seasonal portable restrooms.\n\n- **Bow and Arrow Park**: Found at 3701 N Cochise Dr, Bow and Arrow Park features a playground, half basketball court, picnic tables, and seasonal portable restrooms.\n\n- **Arroyo Park**: Situated at 850 E Ridgecrest Dr, this park offers a playground, youth baseball field, picnic ramada, and seasonal portable restrooms.\n\n- **Guadalupe Park**: Located at 805 W Clay Ave, Guadalupe Park includes a playground, youth softball field, and seasonal portable restrooms.\n\nFor more information, you can visit the [City of Flagstaff's Parks, Recreation, Open Space, and Events Division](https://flagstaff.az.gov/11/Parks-Recreation-Open-Space-and-Events).",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What amenities does Bushmaster Park offer?",
                "role": "user"
            },
            {
                "content": "Bushmaster Park, located at 3150 N Alta Vista Dr in Flagstaff, Arizona, offers a variety of amenities:\n\n- Two playgrounds\n- Two lighted tennis courts\n- Sand volleyball court\n- Two lighted basketball courts\n- Six picnic ramadas\n- Permanent restrooms\n- Skate park\n- Roller skating arena\n- Four horseshoe courts\n- Dog park\n\nThese facilities cater to a wide range of recreational activities for visitors of all ages.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Where is Foxglenn Park located?",
                "role": "user"
            },
            {
                "content": "Foxglenn Park is located at 4200 E Butler Avenue in Flagstaff, Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What features does Buffalo Park have?",
                "role": "user"
            },
            {
                "content": "Buffalo Park, situated at 2400 N Gemini Rd in Flagstaff, Arizona, is a 215-acre open space offering:\n\n- A 2-mile loop trail for walking, running, and wildlife observation\n- Picnic ramada\n- Permanent restrooms\n\nThe park provides scenic views and opportunities for various recreational activities.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Can you tell me about the amenities at Thorpe Park?",
                "role": "user"
            },
            {
                "content": "Thorpe Park, located at 191 N Thorpe Rd in Flagstaff, Arizona, offers a variety of amenities:\n\n- Two playgrounds\n- Four lighted tennis courts plus two additional tennis courts\n- Sand volleyball court\n- One basketball court\n- Two soccer fields\n- Three youth baseball fields\n- Four lighted adult softball fields\n- One picnic ramada\n- Two racquetball courts\n- Disc golf course\n- Dog park\n- Portable and permanent restrooms\n\nThese facilities accommodate a wide range of recreational activities for visitors.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What are some notable lakes in Arizona?",
                "role": "user"
            },
            {
                "content": "Some notable lakes in Arizona include Lake Powell, Lake Mead, Lake Havasu, Theodore Roosevelt Lake, Apache Lake, Canyon Lake, Saguaro Lake, and Bartlett Lake.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Can you tell me about Lake Powell?",
                "role": "user"
            },
            {
                "content": "Lake Powell, located on the Colorado River in northern Arizona and extending into southern Utah, is the second-largest man-made reservoir in the U.S. It boasts nearly 2,000 miles of shoreline and is surrounded by stunning red rock formations, making it a popular destination for boating, fishing, and sightseeing.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What activities can I do at Lake Havasu?",
                "role": "user"
            },
            {
                "content": "At Lake Havasu, you can enjoy boating, fishing, swimming, jet skiing, and camping. The lake is also home to the historic London Bridge, which was relocated from England and reconstructed here, adding a unique sightseeing opportunity.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Where is Theodore Roosevelt Lake located?",
                "role": "user"
            },
            {
                "content": "Theodore Roosevelt Lake is situated in central Arizona, approximately 80 miles northeast of Phoenix. It was formed by the Theodore Roosevelt Dam on the Salt River and is the largest lake entirely within the state.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is unique about Canyon Lake?",
                "role": "user"
            },
            {
                "content": "Canyon Lake, formed by the Mormon Flat Dam on the Salt River, is known for its scenic red rock canyon walls and clear waters. It's a popular spot for boating, fishing, and features the Dolly Steamboat, offering narrated cruises that showcase the area's beauty.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "How many parks are there in Phoenix, Arizona?",
                "role": "user"
            },
            {
                "content": "Phoenix is home to more than 180 parks, offering a wide range of amenities and recreational opportunities. [oai_citation_attribution:5‡City of Phoenix](https://www.phoenix.gov/parks/parks/alphabetical)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is the largest municipal park in Phoenix?",
                "role": "user"
            },
            {
                "content": "South Mountain Park, spanning over 16,500 acres, is the largest municipal park in Phoenix and one of the largest in the world. [oai_citation_attribution:4‡Wikipedia](https://en.wikipedia.org/wiki/Phoenix%2C_Arizona)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Can you name a park in Phoenix known for its hiking trails?",
                "role": "user"
            },
            {
                "content": "Camelback Mountain is renowned for its hiking trails, offering challenging routes and panoramic views of the city. [oai_citation_attribution:3‡Wikipedia](https://en.wikipedia.org/wiki/Phoenix%2C_Arizona)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which park in Phoenix houses the Desert Botanical Garden?",
                "role": "user"
            },
            {
                "content": "Papago Park is home to the Desert Botanical Garden, showcasing desert plant life from around the world. [oai_citation_attribution:2‡Wikipedia](https://en.wikipedia.org/wiki/Phoenix%2C_Arizona)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Where can I find the Phoenix Zoo?",
                "role": "user"
            },
            {
                "content": "The Phoenix Zoo is located within Papago Park in east Phoenix. [oai_citation_attribution:1‡Wikipedia](https://en.wikipedia.org/wiki/Phoenix%2C_Arizona)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is the longest river entirely within Arizona?",
                "role": "user"
            },
            {
                "content": "The Little Colorado River, at approximately 315 miles (507 km) long, is the longest river entirely within Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which river is responsible for carving the Grand Canyon?",
                "role": "user"
            },
            {
                "content": "The Colorado River is responsible for carving the Grand Canyon.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Name a major tributary of the Colorado River in Arizona.",
                "role": "user"
            },
            {
                "content": "The Gila River is a major tributary of the Colorado River in Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which river flows through Phoenix, Arizona?",
                "role": "user"
            },
            {
                "content": "The Salt River flows through Phoenix, Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What river forms part of Arizona's western boundary?",
                "role": "user"
            },
            {
                "content": "The Colorado River forms part of Arizona's western boundary.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which river is known for its turquoise-colored waterfalls in Arizona?",
                "role": "user"
            },
            {
                "content": "Havasu Creek is known for its turquoise-colored waterfalls in Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is the primary river flowing through Tucson, Arizona?",
                "role": "user"
            },
            {
                "content": "The Santa Cruz River is the primary river flowing through Tucson, Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which river in Arizona is a significant tributary to the Gila River?",
                "role": "user"
            },
            {
                "content": "The San Pedro River is a significant tributary to the Gila River in Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Name a river in Arizona that is part of the National Wild and Scenic Rivers System.",
                "role": "user"
            },
            {
                "content": "The Verde River in Arizona is part of the National Wild and Scenic Rivers System.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which river in Arizona has its headwaters in the White Mountains?",
                "role": "user"
            },
            {
                "content": "The Black River has its headwaters in Arizona's White Mountains.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is the largest state park in Arizona?",
                "role": "user"
            },
            {
                "content": "The largest state park in Arizona is Oracle State Park, encompassing approximately 4,000 acres.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which Arizona state park is known for its natural water slide?",
                "role": "user"
            },
            {
                "content": "Slide Rock State Park is renowned for its natural water slide formed by the slippery bed of Oak Creek.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Can you name a state park in Arizona that features a preserved historic mansion?",
                "role": "user"
            },
            {
                "content": "Riordan Mansion State Historic Park in Flagstaff features a preserved historic mansion built in 1904.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which state park in Arizona offers cave tours?",
                "role": "user"
            },
            {
                "content": "Kartchner Caverns State Park offers guided tours of its limestone caves, showcasing impressive stalactites and stalagmites.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What activities can visitors enjoy at Lake Havasu State Park?",
                "role": "user"
            },
            {
                "content": "Visitors to Lake Havasu State Park can enjoy boating, fishing, swimming, and camping along the shores of Lake Havasu.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which Arizona state park is located near the famous London Bridge?",
                "role": "user"
            },
            {
                "content": "Lake Havasu State Park is located near the famous London Bridge in Lake Havasu City.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is unique about Tonto Natural Bridge State Park?",
                "role": "user"
            },
            {
                "content": "Tonto Natural Bridge State Park features a natural travertine bridge that stands 183 feet high and spans 150 feet across Pine Creek.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which state park in Arizona is known for its bird-watching opportunities?",
                "role": "user"
            },
            {
                "content": "Catalina State Park is known for its bird-watching opportunities, with over 150 species recorded within the park.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Can you name a state park in Arizona that preserves a historic courthouse?",
                "role": "user"
            },
            {
                "content": "Tombstone Courthouse State Historic Park preserves the original 1882 courthouse of Tombstone, Arizona.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Which Arizona state park is located at the base of the Superstition Mountains?",
                "role": "user"
            },
            {
                "content": "Lost Dutchman State Park is located at the base of the Superstition Mountains and offers hiking trails with scenic views.",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "How many national parks are there in Arizona?",
                "role": "user"
            },
            {
                "content": "Arizona is home to three national parks: Grand Canyon National Park, Petrified Forest National Park, and Saguaro National Park. [oai_citation_attribution:5‡Dirt In My Shoes](https://www.dirtinmyshoes.com/arizona-national-parks/)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Can you list all the national monuments in Arizona?",
                "role": "user"
            },
            {
                "content": "Arizona has several national monuments, including: Canyon de Chelly, Casa Grande Ruins, Chiricahua, Montezuma Castle, Navajo, Organ Pipe Cactus, Pipe Spring, Sunset Crater Volcano, Tonto, Tuzigoot, Walnut Canyon, and Wupatki. [oai_citation_attribution:4‡American Southwest](https://www.americansouthwest.net/arizona/national-parks.html)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What is unique about Saguaro National Park?",
                "role": "user"
            },
            {
                "content": "Saguaro National Park, located in Tucson, Arizona, is renowned for protecting the nation's largest cacti, the giant saguaro, which is a universal symbol of the American West. [oai_citation_attribution:3‡National Park Service](https://www.nps.gov/state/az/index.htm)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "Where is Petrified Forest National Park located?",
                "role": "user"
            },
            {
                "content": "Petrified Forest National Park is situated in northeastern Arizona, near the town of Holbrook. [oai_citation_attribution:2‡National Park Service](https://www.nps.gov/state/az/index.htm)",
                "role": "assistant"
            }
        ]
    },
    {
        "conversations": [
            {
                "content": "What can visitors see at Walnut Canyon National Monument?",
                "role": "user"
            },
            {
                "content": "Visitors to Walnut Canyon National Monument can explore ancient cliff dwellings nestled within canyon walls, offering insights into the lives of the Sinagua people who inhabited the area over 700 years ago. [oai_citation_attribution:1‡American Southwest](https://www.americansouthwest.net/arizona/national-parks.html)",
                "role": "assistant"
            }
        ]
    }
]


# Convert JSON data to Dataset
dataset = Dataset.from_list(json_data)
for d in dataset:
    pprint(d)
    print("\n")
print(f"Size of dataset: {len(dataset)}")

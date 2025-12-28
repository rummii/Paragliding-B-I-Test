# quiz_data.py
quiz_data = {
    "beginner": {
        "title": "Beginner Paraglider Pilot Quiz",
        "questions": [
            {
                "id": 1,
                "question": "What is the weight of the fabric used to make paraglider canopies? (g/m²)?",
                "options": ["500g/m²", "350g/m²", "35g/m²", "10g/m²"],
                "correct": 2,
                "explanation": "Paraglider canopy fabric typically weighs around 35g/m². This lightweight yet strong material allows for good flight performance while maintaining durability."
            },
            {
                "id": 2,
                "question": "When is the best time to put your legs down during the landing approach?",
                "options": [
                    "As soon as you can see the landing field.",
                    "After you have burned off excessive height and start your landing circuit.",
                    "At the last moment during the landing flare.",
                    "When you are on the final leg of the landing circuit."
                ],
                "correct": 2,
                "explanation": "Your legs should come down at the last moment during the landing flare. This keeps your center of gravity properly positioned throughout the approach and prevents premature weight shift that could affect the flare."
            },
            {
                "id": 3,
                "question": "'Big ears' are a descent technique and serve to increase your descent rate. Additionally, in which situation is pulling 'big ears' a good idea?",
                "options": [
                    "When trying to fly into a strong headwind.",
                    "When flying in turbulent conditions.",
                    "When turning in a small thermal.",
                    "All of the above are correct."
                ],
                "correct": 3,
                "explanation": "Big ears are useful in all these situations: to penetrate headwinds, to reduce turbulence effects by lowering the center of pressure, and to stay in small thermals by increasing descent rate during turns."
            },
            {
                "id": 4,
                "question": "Despite a good flare, you have a lot of speed just before touching down, because you landed with the wind in your back. What do you do?",
                "options": [
                    "You land on your feet and try to run it out during landing.",
                    "You pull in your legs and land on your bum - the foam protector or airbag in your harness will absorb the blow.",
                    "You stretch out your legs and land on your back. This ensures the airbag gives maximum protection.",
                    "On touch down you drop forward and catch the fall with your arms."
                ],
                "correct": 1,
                "explanation": "When landing with tailwind, you have excess ground speed. The safest option is to land on your bum using the harness's protective systems. Attempting to run out could lead to trips and falls."
            },
            {
                "id": 5,
                "question": "What happens when you fly too slowly?",
                "options": [
                    "The wing collapses.",
                    "The glider will enter a deep stall.",
                    "Nothing, you can fly as slow as you want.",
                    "A paraglider glides down through the air. But at what speed?"
                ],
                "correct": 1,
                "explanation": "Flying below minimum speed can cause the glider to enter a deep stall, where it becomes unstable and may not respond normally to control inputs."
            },
            {
                "id": 6,
                "question": "A paraglider glides down through the air. But at what speed?",
                "options": [
                    "The forward speed is over 50 km/h and the sink rate around 10 km/h.",
                    "The forward speed is over 50 km/h and the sink rate around 1 m/s.",
                    "The forward speed is around 35-40 km/h and the sink rate around 1 m/s.",
                    "The forward speed is around 35-40 km/h and the sink rate around 0,1 m/s."
                ],
                "correct": 2,
                "explanation": "Typical paraglider speeds are around 35-40 km/h forward with a sink rate of approximately 1 m/s, giving a glide ratio of about 8:1 to 10:1."
            },
            {
                "id": 7,
                "question": "We lay out the canopy in a semi-circle before take-off. Why?",
                "options": [
                    "This reduces the tendency of the lines to tangle.",
                    "This ensures that the canopy will fill from the middle cells towards the tips.",
                    "This ensures that the outer cells will fill with air first.",
                    "This is the only way you can separate the brake lines from the main lines properly."
                ],
                "correct": 1,
                "explanation": "The semi-circle layout helps ensure that the canopy inflates evenly from the center outward, preventing asymmetric inflation that could lead to control issues during launch."
            },
            {
                "id": 8,
                "question": "You are standing on take-off and you feel the wind coming a bit from the side. Is that a problem for a safe launch?",
                "options": [
                    "Yes that is a problem. We need the wind to be straight from the front to take off safely.",
                    "Up to about 45 degrees is usually not a problem. You lay out the wing facing the wind and during the acceleration phase you correct your course to fly away straight from the take-off.",
                    "Up to about 45 degrees is usually not a problem. You lay out the wing straight down the take-off and correct the wing during the inflation phase.",
                    "Up to about 90 degrees is usually not a problem. You lay out the wing straight down the take-off and correct the wing during the inflation phase."
                ],
                "correct": 1,
                "explanation": "Crosswinds up to 45 degrees are manageable. Face the wing into the wind during layout, then adjust your run direction during acceleration to achieve a straight takeoff path."
            },
            {
                "id": 9,
                "question": "During daily inspections you notice a tear of about 2.5cm or one inch in the canopy of your paraglider. What do you do?",
                "options": [
                    "1 is correct.",
                    "2 is correct.",
                    "Neither 1 nor 2 are correct.",
                    "1. is a temporary solution, go for 2. as soon as possible."
                ],
                "correct": 3,
                "explanation": "A 2.5cm tear should be professionally repaired. While temporary repair tape might work short-term, proper sewing by a certified technician ensures structural integrity and safety."
            },
            {
                "id": 10,
                "question": "What do we call the risers that are connected to the lines running to the leading edge of the canopy?",
                "options": ["A-risers", "B-risers", "C-risers", "D-risers"],
                "correct": 0,
                "explanation": "A-risers connect to the leading edge lines and control the angle of attack. They're crucial for speed control and stall prevention."
            }
        ]
    },
    "progressive": {
        "title": "Progressive Pilot Quiz",
        "questions": [
            {
                "id": 1,
                "question": "Most paragliders nowadays have short rods in the leading edge. Why are these there?",
                "options": [
                    "They are needed to give the canopy its strength.",
                    "They ensure a better resistance to collapses.",
                    "They are required for the certification of the glider.",
                    "They facilitate the inflation of the glider during take-off."
                ],
                "correct": 3,
                "explanation": "Leading edge rods (sometimes called battens) help maintain the wing's profile and facilitate clean inflation, especially in challenging wind conditions."
            },
            {
                "id": 2,
                "question": "At 500m above the landing field you notice that your glider has entered a deep stall. What is the best thing to do?",
                "options": [
                    "Start turning using weight shift so the paraglider can gain speed again.",
                    "Pull down both brakes fully and let them up again.",
                    "Do nothing for at least a couple of seconds.",
                    "Carefully push the front risers forward until the glider starts to gain speed again."
                ],
                "correct": 3,
                "explanation": "In a deep stall, carefully pushing the front risers forward reduces the angle of attack and allows the wing to regain flying speed. This should be done gently to avoid diving."
            },
            {
                "id": 3,
                "question": "What information can the isobars on a weather chart tell us?",
                "options": [
                    "The location of high and low pressure areas.",
                    "Wind direction and wind speed, as well as the location of high and low pressure areas.",
                    "Information about wind and temperature.",
                    "The course of jet streams."
                ],
                "correct": 1,
                "explanation": "Isobars show pressure gradients. Closer isobars indicate stronger winds, and their pattern shows wind direction (parallel to isobars) and pressure systems."
            },
            {
                "id": 4,
                "question": "During which part of the flight is the angle of attack so large that the airflow around the airfoil is no longer laminar but instead 'breaks' and becomes turbulent?",
                "options": [
                    "During take-off",
                    "During a spiral dive",
                    "While flying in dynamic lift",
                    "While flaring to land"
                ],
                "correct": 3,
                "explanation": "During flare, the angle of attack increases significantly to reduce descent rate. At extreme angles, airflow separates causing turbulent flow over the wing."
            },
            {
                "id": 5,
                "question": "How can you recognize an approaching cold front?",
                "options": [
                    "The appearance of large, quickly growing cumulonimbus clouds at the horizon.",
                    "By cirrus clouds high up.",
                    "By the presence of powerful updrafts and unusually large cumulus clouds.",
                    "All of the above."
                ],
                "correct": 3,
                "explanation": "Cold fronts are often preceded by high cirrus clouds, followed by developing cumulus/cumulonimbus with strong updrafts as the front approaches."
            },
            {
                "id": 6,
                "question": "What is the approximate minimum breaking strength of a tow line?",
                "options": ["1 N", "1 kN", "6 N", "6 kN"],
                "correct": 3,
                "explanation": "Tow lines typically have minimum breaking strengths around 6 kN (approx 600kg) to safely handle the forces during aerotow launches."
            },
            {
                "id": 7,
                "question": "Your wing collapses on the right hand side. What is the first thing you do?",
                "options": [
                    "A quick pump of the right brake to open the canopy quickly.",
                    "A quick pump on the left brake so the canopy can fill with air from the cells that are still open.",
                    "Pull both brakes simultaneously and release again.",
                    "Keep your course using weight-shift and brake."
                ],
                "correct": 0,
                "explanation": "A quick, controlled pump on the collapsed side's brake helps reinflate the wing by encouraging airflow back into the collapsed cells."
            },
            {
                "id": 8,
                "question": "Which of these instruments is suitable to measure groundspeed?",
                "options": ["GPS", "TAS", "Anemometer", "Variometer"],
                "correct": 0,
                "explanation": "GPS measures groundspeed directly by tracking position changes over time relative to the ground. Anemometers measure airspeed, not groundspeed."
            },
            {
                "id": 9,
                "question": "What is the air pressure at sea level and how does the air pressure change with altitude?",
                "options": [
                    "It can vary by more than 100hPa at sea level and is halved every 3500m.",
                    "It is always 1013,25hPa at sea level and is halved every 5500m.",
                    "On average 1013,25hPa at sea level and decreases linearly with altitude.",
                    "On average 1013,25hPa at sea level and is halved every 5500m."
                ],
                "correct": 3,
                "explanation": "Standard sea level pressure is 1013.25 hPa, and pressure approximately halves every 5.5km (18,000ft) due to the exponential nature of atmospheric pressure decrease."
            },
            {
                "id": 10,
                "question": "What is katabatic wind?",
                "options": [
                    "Wind that is caused by a high pressure area.",
                    "Wind that is caused by air flowing down a mountain under the influence of gravity.",
                    "Valley wind.",
                    "Wind caused by a temperature gradient."
                ],
                "correct": 1,
                "explanation": "Katabatic winds occur when cold, dense air flows downhill under gravity, often at night as mountain slopes cool. The opposite (upslope) flow is anabatic wind."
            }
        ]
    }
}

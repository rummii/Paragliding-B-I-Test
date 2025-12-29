# quiz_data.py - Complete version with all questions
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
                    "Nothing, you can fly as slow as you want."
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
                "question": "During daily inspections you notice a tear of about 2.5cm or one inch in the canopy of your paraglider. What do you do?\n1. You fix the tear with ripstop tape on both sides of the fabric.\n2. You take the glider to a dealer or manufacturer to have it professionally repaired.",
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
            },
            {
                "id": 11,
                "question": "For a paraglider in the mountains, what wind speeds are considered safe to fly?",
                "options": [
                    "Only nil winds from 0 to 1 Bft.",
                    "Only light winds from 2 to 3 Bft.",
                    "Only with wind from 0 up to 3 Bft.",
                    "Only with wind speeds over 3 Bft."
                ],
                "correct": 1,
                "explanation": "Light winds (2-3 Bft, approximately 6-20 km/h) are generally considered safe for mountain flying. Stronger winds can create dangerous turbulence and difficult landing conditions."
            },
            {
                "id": 12,
                "question": "What happens when you brake a paraglider so much that the air speed falls below the minimum speed of about 25km/h?",
                "options": [
                    "The glider stalls, ie it doesn't fly anymore.",
                    "The glider will fly on as slow as you want.",
                    "The glider collapses."
                ],
                "correct": 0,
                "explanation": "When airspeed falls below minimum speed (stall speed), the wing loses lift and stalls. Recovery requires releasing brakes to regain speed."
            },
            {
                "id": 13,
                "question": "What part in a paraglider is an internal fabric support that runs diagonally across the cells?",
                "options": ["A cell", "A top line", "A diagonal rib", "A stabilo"],
                "correct": 2,
                "explanation": "Diagonal ribs provide structural support and help maintain the wing's aerofoil shape across the span of the canopy."
            },
            {
                "id": 14,
                "question": "Standing on launch you see a rain shower approaching. Do you take off?",
                "options": [
                    "No, flying in the rain is illegal under air law.",
                    "Yes, paragliders are not affected by rain and the accompanying wind will dry the paraglider quickly.",
                    "Yes, if you can be sure that you have landed before the rain shower arrives.",
                    "No, rain showers are often accompanied by wind gusts, which can be very dangerous for paragliders. Additionally, a wet canopy is more dangerous to fly."
                ],
                "correct": 3,
                "explanation": "Rain showers bring unpredictable wind gusts and turbulence. Wet canopies can experience reduced performance, increased weight, and altered flight characteristics."
            },
            {
                "id": 15,
                "question": "How tight do you need to pull the leg straps of the harness?",
                "options": [
                    "As tight as possible so you won't fall out of the harness and you won't move from side to side in a turn.",
                    "As loose as they will go so you can easily accelerate during take-off and the circulation in your legs is not hindered.",
                    "That doesn't matter, as long as the buckles are secure.",
                    "They need to be loose enough that your flat hand can just fit between the straps and your legs. That way your movements aren't hindered too much and you can still get into the harness easily after take-off."
                ],
                "correct": 3,
                "explanation": "Proper leg strap tension allows one flat hand to fit between strap and leg. This provides security while allowing blood circulation and movement freedom."
            },
            {
                "id": 16,
                "question": "Which pre-launch check is the most important?",
                "options": [
                    "Checking the lines and canopy are laid out cleanly.",
                    "Checking your flight instruments.",
                    "Checking your leg straps are fastened.",
                    "Checking if there is sufficient thermal activity."
                ],
                "correct": 2,
                "explanation": "Fastening leg straps is the most critical pre-launch check. An unfastened harness could lead to falling out during flight, which is potentially fatal."
            },
            {
                "id": 17,
                "question": "You just landed. What do you do?",
                "options": [
                    "You bundle up the glider in a 'field pack' and take the shortest way to the designated packing area.",
                    "You bundle up the glider in a 'field pack' and take the shortest way to the edge of the field and from there to the designated packing area.",
                    "You report to the instructor. When he or she says it's ok, you bundle up the glider in a 'field pack' and walk to the designated packing area.",
                    "You pack up your vulnerable glider on the spot and then you report to the instructor."
                ],
                "correct": 2,
                "explanation": "After landing, first report to the instructor for debriefing and permission to pack up. Then create a field pack and walk to the designated packing area without dragging the glider."
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
                "question": "What is the name of the line indicated with G in this illustration?",
                "options": ["Main line", "Top line", "Brake line", "Stabilo line"],
                "correct": 3,
                "explanation": "Stabilo lines help maintain the wing's stability and are part of the internal line structure connecting various parts of the canopy."
            },
            {
                "id": 9,
                "question": "Which of these instruments is suitable to measure groundspeed?",
                "options": ["GPS", "TAS", "Anemometer", "Variometer"],
                "correct": 0,
                "explanation": "GPS measures groundspeed directly by tracking position changes over time relative to the ground. Anemometers measure airspeed, not groundspeed."
            },
            {
                "id": 10,
                "question": "You are flying on tow when suddenly the tow line snaps somewhere down low. Do you keep flying with the rest of the line still attached to your harness?",
                "options": [
                    "Yes, you can ignore the line because it doesn't influence the flying characteristics of your paraglider.",
                    "No, because the weight of the line will drag you down.",
                    "No, because the friction of the line over the ground will pull you down.",
                    "No, because the line can get stuck on an object such as a tree or a pole."
                ],
                "correct": 3,
                "explanation": "A dangling tow line can snag on obstacles, causing sudden and potentially dangerous pulls on the glider. It should be released if possible."
            },
            {
                "id": 11,
                "question": "After take-off you notice that you need to pull quite a bit of right brake to ensure the paraglider flies straight ahead. What is going on?",
                "options": [
                    "There is a strong wind from the right.",
                    "There is a strong wind from the left.",
                    "You have a knot in the C-lines on the right side.",
                    "You have a knot in the C-lines on the left side."
                ],
                "correct": 3,
                "explanation": "A knot in the C-lines on one side effectively shortens those lines, causing asymmetric drag that requires opposite brake input to compensate."
            },
            {
                "id": 12,
                "question": "Which distance must a paraglider keep with respect to other aircraft?",
                "options": ["Enough distance", "At least 50m", "At least 150m", "At least 300m"],
                "correct": 2,
                "explanation": "International air regulations typically require paragliders to maintain at least 150m separation from other aircraft for safety."
            },
            {
                "id": 13,
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
                "id": 14,
                "question": "What is the effect of flying at high altitudes on the descent rate of a paraglider?",
                "options": [
                    "The descent rate decreases with altitude.",
                    "Altitude has no influence on the descent rate.",
                    "The descent rate increases with altitude.",
                    "None of the above is true."
                ],
                "correct": 2,
                "explanation": "At higher altitudes, thinner air provides less lift and drag, resulting in increased sink rates and generally poorer glide performance."
            },
            {
                "id": 15,
                "question": "What is the aspect ratio of a wing with a span of 10 meters and a flat surface of 20 square meters?",
                "options": ["0.5", "2.0", "5.0", "40"],
                "correct": 2,
                "explanation": "Aspect ratio = (span²) / area = (10²) / 20 = 100 / 20 = 5. Higher aspect ratios generally indicate better glide performance but less stability."
            },
            {
                "id": 16,
                "question": "What is katabatic wind?",
                "options": [
                    "Wind that is caused by a high pressure area.",
                    "Wind that is caused by air flowing down a mountain under the influence of gravity.",
                    "Valley wind.",
                    "Wind caused by a temperature gradient."
                ],
                "correct": 1,
                "explanation": "Katabatic winds occur when cold, dense air flows downhill under gravity, often at night as mountain slopes cool. The opposite (upslope) flow is anabatic wind."
            },
            {
                "id": 17,
                "question": "Which lines have the following properties: sensitive to bending, heat resistant, yellowish colour?",
                "options": ["Dyneema lines", "Kevlar lines", "Polyester lines", "Nylon lines"],
                "correct": 1,
                "explanation": "Kevlar lines are known for their heat resistance, yellowish color, and sensitivity to bending fatigue. They require careful handling and regular inspection."
            },
            {
                "id": 18,
                "question": "What is the effect of an increased porosity of the canopy on the flight behavior of the paraglider?",
                "options": [
                    "The paraglider is more difficult to control and becomes unstable around its yaw axis.",
                    "The flying speed increases, therefore collapses are more likely.",
                    "The flying speed decreases independent of how much brake is applied, resulting in a flat polar curve.",
                    "The stall speed increases as well as the risk to enter a deep stall."
                ],
                "correct": 0,
                "explanation": "Increased canopy porosity allows more air to pass through the fabric, reducing pressure differential and making the wing less stable, particularly in yaw (side-to-side) movement."
            }
        ]
    }
}

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

question_words = {

    "definition": (
        "what is",
        "what are",
        "what does",
        "what do",
        "tell me about",
        "explain",
        "define",
        "meaning of",
        "what exactly is"
    ),

    "uses": (
        "use",
        "uses",
        "used for",
        "what is it used for",
        "what are the uses",
        "what can i use",
        "where is it used",
        "why is it used",
        "purpose",
        "what is the purpose"
    ),

    "types": (
        "type",
        "types",
        "kind",
        "kinds",
        "different types",
        "different kinds",
        "varieties",
        "what types",
        "what kinds"
    ),

    "characteristics": (
        "characteristic",
        "characteristics",
        "features",
        "feature",
        "properties",
        "qualities",
        "what is it like",
        "what makes it different"
    ),

    "advantages": (
        "advantage",
        "advantages",
        "benefit",
        "benefits",
        "pros",
        "good things",
        "good points",
        "why is it good",
        "positive points"
    ),

    "disadvantages": (
        "disadvantage",
        "disadvantages",
        "drawback",
        "drawbacks",
        "cons",
        "bad things",
        "bad points",
        "problems",
        "limitations",
        "negative points"
    ),

    "how_to_use": (
        "how to use",
        "how do i use",
        "how can i use",
        "how should i use",
        "how do you use",
        "way to use"
    ),

    "how_to_make": (
        "how to make",
        "how do i make",
        "how can i make",
        "how should i make",
        "what colors make",
        "what colour makes",
        "how to create",
        "how do i create",
        "how can i create",
        "make this color",
        "make this colour",
        "create this color",
        "create this colour"
    ),

    "steps": (
        "steps",
        "step by step",
        "how to paint",
        "how do i paint",
        "how can i paint",
        "how should i paint",
        "painting process",
        "process of painting"
    ),

    "materials": (
        "material",
        "materials",
        "what do i need",
        "what is needed",
        "things needed",
        "things required",
        "supplies",
        "equipment",
        "painting supplies"
    ),

    "beginner": (
        "beginner",
        "beginners",
        "good for beginners",
        "suitable for beginners",
        "easy for beginners",
        "best for beginners",
        "should a beginner use"
    ),

    "expert": (
        "expert",
        "experts",
        "advanced",
        "professional",
        "professionals",
        "advanced users",
        "best for experts"
    ),

    "comparison": (
        "better",
        "worse",
        "best",
        "worst",
        "which is better",
        "which is worse",
        "which one is better",
        "which one is worse",
        "compare",
        "comparison",
        "difference",
        "differences",
        "diff",
        "diff btw",
        "difference between",
        "better than",
        "worse than"
    ),

    "techniques": (
        "technique",
        "techniques",
        "method",
        "methods",
        "different techniques",
        "different methods",
        "painting methods"
    ),

    "tips": (
        "tip",
        "tips",
        "advice",
        "advise",
        "suggestion",
        "suggestions",
        "recommend",
        "recommendation",
        "what should i know",
        "what do you recommend"
    ),

    "care": (
        "care",
        "clean",
        "cleaning",
        "clean it",
        "store",
        "storage",
        "maintain",
        "maintenance",
        "how to take care"
    ),

    "difficulty": (
        "difficult",
        "difficulty",
        "hard",
        "easy",
        "is it easy",
        "is it difficult",
        "is it hard",
        "how difficult",
        "how easy"
    ),

    "drying": (
        "dry",
        "drying",
        "how long does it take to dry",
        "how fast does it dry",
        "does it dry quickly",
        "dry quickly"
    ),

    "cost": (
        "cost",
        "price",
        "expensive",
        "cheap",
        "cheaper",
        "how much",
        "affordable"
    ),

    "suitable_for": (
        "suitable for",
        "good for",
        "best for",
        "who can use",
        "who is it for",
        "which is good for"
    ),

    "feelings": (
        "feeling",
        "feelings",
        "emotion",
        "emotions",
        "how does it make you feel",
        "what feelings",
        "what emotions",
        "emotional benefits"
    ),

    "happy": (
        "happy",
        "happiness",
        "joy",
        "joyful",
        "cheerful",
        "positive mood",
        "feel happier",
        "make me happy",
        "good mood",
        "feel good"
    ),

    "sad": (
        "sad",
        "sadness",
        "unhappy",
        "low mood",
        "feel sad",
        "feeling down",
        "when i am sad",
        "painting when sad"
    ),

    "relaxation": (
        "relax",
        "relaxing",
        "relaxation",
        "peace",
        "peaceful",
        "calm",
        "calming",
        "stress",
        "stress relief",
        "reduce stress",
        "feel calm",
        "help me relax"
    ),

    "greeting": (
        "hello",
        "hi",
        "hey",
        "hii",
        "hiii",
        "hey there",
        "good morning",
        "good afternoon",
        "good evening"
    ),

    "goodbye": (
        "bye",
        "goodbye",
        "see you",
        "see you later",
        "talk to you later"
    )
}

painting_knowledge = {

    "colors": {
        "definition": "Colors are an important part of painting and can be mixed, combined, and adjusted to create different shades, tints, tones, and visual effects.",
        "types": "The basic color groups commonly discussed in painting are primary, secondary, and tertiary colors.",
        "uses": "Colors are used to create mood, depth, contrast, lighting, shadows, highlights, and visual interest in paintings.",
        "how_to_make": "Many colors can be created by mixing other colors. Red and yellow make orange, yellow and blue make green, and red and blue can make purple.",
        "comparison": "There is no single best color for every painting. The best color depends on your subject, mood, lighting, and style. Warm colors such as red, orange, and yellow can create energetic or warm feelings, while cool colors such as blue, green, and violet can create calm or peaceful effects.",
        "tips": "Start by mixing small amounts of paint. Experiment with different ratios to create lighter, darker, warmer, and cooler variations."
    },

    "painting": {
        "definition": "Painting is the art of applying colors, shapes, and marks to a surface to create an image, express an idea, or communicate emotions.",
        "purpose": "People use painting for creativity, self-expression, communication, decoration, storytelling, learning, and artistic exploration.",
        "feelings": "Painting can help people express emotions and may feel relaxing, enjoyable, satisfying, peaceful, or calming.",
        "types": "Common forms include portrait painting, landscape painting, still life, abstract painting, realism, impressionism, and decorative painting.",
        "techniques": "Painting techniques include blending, layering, dry brushing, glazing, wet-on-wet, wet-on-dry, scumbling, stippling, and impasto.",
        "materials": "Basic painting materials include paint, brushes, a suitable surface, palette, water container, and cloth or paper towel.",
        "steps": "A basic painting process is to choose a subject, prepare the surface, sketch the main shapes, block in large colors, add shadows and highlights, refine details, and allow the painting to dry.",
        "advantages": "Painting encourages creativity, develops observation and hand control, provides a way to express ideas, and can be an enjoyable creative activity.",
        "tips": "Beginners can start with simple subjects, basic colors, inexpensive materials, and a few fundamental techniques.",
        "difficulty": "Painting is easy to start but improving brush control, color mixing, proportions, and techniques requires practice."
    },

    "paints": {
        "definition": "Paint is a material containing pigment and a medium that is applied to a surface to add color and create artwork.",
        "uses": "Paint is used for artwork, illustration, decoration, design, crafts, and creative projects.",
        "types": "Common types include acrylic, oil, watercolor, gouache, tempera, and poster paint.",
        "comparison": "Acrylic dries quickly and is versatile, oil dries slowly and allows long blending, watercolor is transparent, and gouache is generally opaque with a matte finish.",
        "materials": "Paintings may require paint, brushes, a suitable surface, palette, water or appropriate medium, and cleaning materials.",
        "beginner": "Acrylic, watercolor, and gouache can all be suitable starting points depending on the artist's preferred style and materials.",
        "cost": "Painting costs vary widely. Beginners can start with affordable student-grade paints and a small set of basic supplies."
    },

    "acrylic": {
        "definition": "Acrylic paint is a water-based paint made from pigment suspended in an acrylic polymer medium. It dries relatively quickly and becomes water-resistant when dry.",
        "uses": "Acrylic can be used for canvas painting, illustrations, crafts, decorative artwork, landscapes, portraits, and mixed-media projects.",
        "characteristics": "Acrylic is versatile, fast-drying, water-mixable when wet, and available in different consistencies and finishes.",
        "advantages": "Acrylic dries quickly, is versatile, can be diluted with water, works on many prepared surfaces, and supports many techniques.",
        "disadvantages": "Its quick drying time can make long blending difficult, and dried acrylic can be difficult to remove from some tools or surfaces.",
        "how_to_use": "Apply acrylic with suitable brushes, palette knives, sponges, or other tools. It can be used thinly with water or in thicker layers.",
        "beginner": "Acrylic is generally a convenient choice for beginners because it is versatile, relatively easy to handle, and dries quickly.",
        "expert": "Experienced artists can use acrylic for detailed layering, glazing, texture, mixed media, and experimental techniques.",
        "techniques": "Acrylic can be used for blending, layering, dry brushing, glazing, scumbling, stippling, and impasto.",
        "care": "Clean brushes and tools while acrylic is still wet. Keep paint containers closed when not in use.",
        "materials": "Basic acrylic painting materials include acrylic paints, brushes, a suitable surface, palette, water container, and cloth or paper towel.",
        "difficulty": "Acrylic is generally beginner-friendly, although techniques such as smooth blending can require practice.",
        "drying": "Acrylic usually dries relatively quickly, although drying time depends on paint thickness, humidity, temperature, and the surface.",
        "cost": "Acrylic paint is available in both affordable student-grade and more expensive artist-grade options."
    },

    "oil": {
        "definition": "Oil paint is made from pigment mixed with a drying oil, commonly linseed oil.",
        "uses": "Oil paint is commonly used for portraits, landscapes, still life, realistic artwork, and detailed paintings.",
        "characteristics": "Oil paint dries slowly, has rich color, and allows artists to blend and modify paint for an extended period.",
        "advantages": "Its slow drying time allows extended blending, subtle transitions, layering, and detailed work.",
        "disadvantages": "Oil paint generally dries much more slowly than acrylic and requires careful cleaning and handling of painting materials.",
        "how_to_use": "Oil paint can be applied with brushes or palette knives. Artists often build paintings through layers or work directly while the paint is wet.",
        "beginner": "Oil painting can be learned by beginners, but it may require more patience and understanding of materials than acrylic.",
        "expert": "Oil paint offers experienced artists extensive control over blending, glazing, layering, texture, and detailed color transitions.",
        "techniques": "Oil painting techniques include glazing, scumbling, impasto, blending, alla prima, and layering.",
        "materials": "Oil painting commonly requires oil paints, suitable brushes, a palette, a prepared surface, and appropriate cleaning materials.",
        "difficulty": "Oil painting can have a steeper learning curve because of its slow drying time and more involved material handling.",
        "drying": "Oil paint dries slowly compared with acrylic. Drying time varies with pigment, layer thickness, environment, and materials used.",
        "cost": "Oil painting can become more expensive because it may require additional materials and suitable cleaning supplies."
    },

    "watercolor": {
        "definition": "Watercolor is a transparent water-based paint made from pigment and a water-soluble binder.",
        "uses": "Watercolor is commonly used for landscapes, illustrations, sketches, studies, travel paintings, and expressive artwork.",
        "characteristics": "Watercolor is transparent, fluid, lightweight, and strongly influenced by the amount of water used.",
        "advantages": "Watercolors are portable, require relatively few materials, and can create delicate transparent effects.",
        "disadvantages": "Correcting mistakes can be difficult because the paint is transparent and the paper often remains an important part of the image.",
        "how_to_use": "Mix watercolor with water and apply it to suitable watercolor paper using appropriate brushes.",
        "beginner": "Watercolor can be beginner-friendly, although controlling water and achieving clean results requires practice.",
        "expert": "Experienced artists can use watercolor for controlled washes, detailed illustrations, expressive effects, and complex transparent layering.",
        "techniques": "Watercolor techniques include wet-on-wet, wet-on-dry, washes, glazing, lifting, and dry brush.",
        "materials": "Basic watercolor materials include watercolor paints, watercolor paper, brushes, water, and a palette.",
        "difficulty": "Watercolor can be challenging because controlling water and correcting mistakes requires practice.",
        "drying": "Watercolor dries relatively quickly, although drying time depends on the amount of water and environmental conditions.",
        "cost": "Watercolor can be inexpensive to start because a small paint set, brushes, paper, and water are often enough."
    },

    "gouache": {
        "definition": "Gouache is a water-based paint that is generally more opaque than watercolor and can create a matte finish.",
        "uses": "Gouache is used for illustration, design, posters, studies, decorative artwork, and paintings requiring strong opaque color.",
        "characteristics": "Gouache is opaque, water-based, reworkable with water to some extent, and usually dries to a matte appearance.",
        "advantages": "Gouache provides strong opaque colors and can create both bold flat areas and detailed artwork.",
        "disadvantages": "Color can change as gouache dries, and thick layers may crack or become disturbed when rewetted.",
        "how_to_use": "Mix gouache with water to adjust its consistency and apply it using suitable brushes to appropriate paper or surfaces.",
        "beginner": "Gouache can be a good choice for beginners who want more opaque colors than watercolor provides.",
        "expert": "Experienced artists can use gouache for illustration, graphic compositions, detailed studies, and controlled color work.",
        "techniques": "Gouache can be used for layering, flat washes, blending, dry brushing, and controlled opaque painting.",
        "materials": "Basic gouache painting requires gouache paints, suitable paper, brushes, water, and a palette.",
        "difficulty": "Gouache is accessible to beginners but controlling its consistency and opacity takes practice."
    },

    "brushes": {
        "definition": "A paintbrush is a tool used to apply, spread, blend, and manipulate paint on a surface.",
        "uses": "Brushes are used for filling areas, creating lines, blending colors, adding details, and producing different textures.",
        "types": "Common brush shapes include round, flat, filbert, fan, angle, mop, and liner brushes.",
        "characteristics": "Brushes differ in shape, size, stiffness, softness, and bristle material.",
        "comparison": "Round brushes are versatile for details and lines, flat brushes are useful for broad strokes, and filbert brushes are useful for softer edges and blending.",
        "beginner": "Beginners can start with a round brush, flat brush, and medium-sized detail brush.",
        "care": "Clean brushes after use, avoid leaving them sitting in water for long periods, and store them without crushing their bristles.",
        "tips": "Use larger brushes for broad areas and smaller brushes for details."
    },

    "round_brush": {
        "definition": "A round brush has a rounded tip and is one of the most versatile painting brushes.",
        "uses": "Round brushes can be used for lines, details, small areas, curves, and controlled strokes.",
        "characteristics": "Round brushes come in many sizes and can produce both thin and broader strokes depending on pressure.",
        "beginner": "A medium-sized round brush is useful for beginners because it can perform many basic tasks.",
        "advantages": "Round brushes are versatile and useful for both detail work and moderate coverage.",
        "care": "Clean the bristles after use and reshape the tip while the brush is clean.",
        "tips": "Experiment with different pressure levels to learn how the same round brush can create different marks."
    },

    "flat_brush": {
        "definition": "A flat brush has a broad, flat-shaped tip designed for wider strokes and defined edges.",
        "uses": "Flat brushes are useful for filling large areas, creating straight edges, broad strokes, and certain blending techniques.",
        "characteristics": "Flat brushes have a wide surface that can hold a relatively large amount of paint.",
        "beginner": "A medium flat brush is useful for beginners when covering backgrounds or larger areas.",
        "advantages": "Flat brushes cover areas efficiently and can produce both broad and edge-focused strokes.",
        "care": "Clean the entire brush and avoid allowing paint to dry between the bristles.",
        "tips": "Use the broad side for coverage and the narrow edge for thinner marks."
    },

    "filbert_brush": {
        "definition": "A filbert brush has a flat body with a rounded tip, combining some properties of flat and round brushes.",
        "uses": "Filbert brushes are useful for soft edges, blending, curved shapes, and natural-looking forms.",
        "characteristics": "The rounded tip creates softer marks than a typical flat brush.",
        "beginner": "Filbert brushes can be useful after beginners understand basic brush control.",
        "expert": "Experts often use filberts for portraits, organic shapes, soft blending, and controlled transitions.",
        "advantages": "They can create both broad strokes and softer edges.",
        "care": "Clean the brush thoroughly and reshape the rounded tip after cleaning."
    },

    "canvas": {
        "definition": "Canvas is a painting surface commonly made from woven fabric stretched over a frame or attached to a rigid support.",
        "uses": "Canvas is commonly used for acrylic, oil, and many other forms of painting.",
        "types": "Common canvas formats include stretched canvas, canvas board, canvas panels, and canvas pads.",
        "characteristics": "Canvas can vary in texture, weight, size, flexibility, and surface preparation.",
        "advantages": "Canvas is durable, available in many sizes, and suitable for many painting styles.",
        "disadvantages": "Large or high-quality canvases can be more expensive, and some canvas surfaces require proper preparation.",
        "beginner": "Beginners can use small pre-prepared canvas boards or stretched canvases because they are convenient and easy to handle.",
        "materials": "Canvas is commonly made from cotton or linen fabric attached to a frame or rigid support.",
        "care": "Keep finished canvas artwork clean, dry, and protected from excessive moisture and physical damage.",
        "tips": "For beginners, starting with a small pre-prepared canvas is usually easier than preparing a large canvas from scratch."
    },

    "stretched_canvas": {
        "definition": "Stretched canvas is fabric stretched and secured over a wooden frame.",
        "uses": "It is commonly used for finished paintings and can support acrylic and oil painting.",
        "advantages": "It provides a traditional painting surface and is available in many sizes."
    },

    "canvas_board": {
        "definition": "Canvas board is canvas fabric mounted on a rigid board.",
        "uses": "It is commonly used for practice, studies, and finished paintings.",
        "advantages": "Canvas board is convenient, portable, and generally less expensive than stretched canvas."
    },

    "techniques": {
        "definition": "Painting techniques are different methods artists use to apply, blend, layer, texture, or manipulate paint.",
        "types": "Common techniques include blending, layering, dry brushing, glazing, wet-on-wet, wet-on-dry, scumbling, stippling, and impasto.",
        "beginner": "Beginners can start with simple techniques such as basic blending, layering, dry brushing, and simple washes.",
        "expert": "Experienced artists can combine multiple techniques such as glazing, impasto, scumbling, controlled blending, and layering."
    },

    "blending": {
        "definition": "Blending is a painting technique where colors are gradually mixed together to create smooth transitions.",
        "uses": "Blending is useful for skies, gradients, shadows, highlights, portraits, and smooth color transitions.",
        "beginner": "Beginners can practice blending two similar colors before trying more complicated gradients.",
        "tips": "Work before the paint becomes completely dry when using paints that allow wet blending."
    },

    "layering": {
        "definition": "Layering is the process of applying one layer of paint over another to build color, depth, details, or texture.",
        "uses": "Layering can be used to build shadows, highlights, depth, textures, and complex color relationships.",
        "beginner": "Beginners can start with a simple base layer and gradually add darker and lighter areas."
    },

    "dry_brushing": {
        "definition": "Dry brushing is a technique where a brush contains relatively little paint or moisture, producing broken and textured marks.",
        "uses": "Dry brushing can create texture for hair, grass, wood, rocks, fabric, and other surfaces.",
        "beginner": "It is a useful technique for beginners because it can create interesting textures without requiring perfectly smooth strokes."
    },

    "impasto": {
        "definition": "Impasto is a technique where paint is applied in thick layers so that brush or palette-knife marks remain visible.",
        "uses": "Impasto is useful for creating strong texture, raised marks, and expressive surfaces.",
        "expert": "Experienced artists can control paint thickness and tool direction to create intentional textures and visual effects."
    },

    "color_mixing": {
        "definition": "Color mixing is the process of combining different paint colors to create new colors, shades, tints, and tones.",
        "tips": "Mix small amounts first because adding too much of one color can quickly change the mixture.",
        "types": "Primary colors are commonly taught as red, yellow, and blue. Secondary colors include orange, green, and purple."
    },

    "yellow": {
        "definition": "Yellow is a bright primary color commonly used in painting for light, warmth, highlights, flowers, and sunlight.",
        "how_to_make": "Yellow is generally a primary paint color, so it cannot normally be made by mixing other basic paint colors. You usually need yellow paint.",
        "uses": "Yellow can be used for sunlight, flowers, highlights, warm backgrounds, and bright objects.",
        "tips": "Mix yellow with white to create a lighter yellow. Small amounts of orange can make it warmer."
    },

    "orange": {
        "definition": "Orange is a warm color created by combining red and yellow.",
        "how_to_make": "Mix yellow and red to make orange. More yellow creates a yellower orange, while more red creates a redder orange.",
        "shades": "Add white to create a lighter orange."
    },

    "green": {
        "definition": "Green is a secondary color commonly created by mixing yellow and blue.",
        "how_to_make": "Mix yellow and blue to make green. More yellow creates a warmer yellow-green, while more blue creates a cooler blue-green.",
        "shades": "Add white to create a lighter green."
    },

    "purple": {
        "definition": "Purple is a color commonly created by combining red and blue.",
        "how_to_make": "Mix red and blue to make purple. Adjust the amount of each color to change the result.",
        "shades": "Add white to create lighter purple or lavender."
    },

    "violet": {
        "definition": "Violet is a cool purple color often created by mixing suitable red and blue pigments.",
        "how_to_make": "Mix suitable red and blue paints. The exact violet depends on the pigments being used."
    },

    "brown": {
        "definition": "Brown is a warm neutral color commonly used for wood, soil, skin tones, shadows, and natural subjects.",
        "how_to_make": "Brown can be created by mixing complementary colors such as red and green, blue and orange, or yellow and purple.",
        "shades": "Add white for a lighter brown or adjust the mixture with small amounts of the original colors."
    },

    "pink": {
        "definition": "Pink is a lighter tint of red.",
        "how_to_make": "Mix red with white to create pink. More white creates a lighter pink, while more red creates a stronger pink.",
        "uses": "Pink can be used for flowers, skin tones, clothing, backgrounds, highlights, and decorative artwork."
    },

    "light_blue": {
        "definition": "Light blue is a lighter version of blue.",
        "how_to_make": "Mix blue with white to create light blue. Add more white for a paler blue."
    },

    "dark_blue": {
        "definition": "Dark blue is a deeper version of blue.",
        "how_to_make": "Start with blue and gradually add a small amount of a suitable darker color to deepen it."
    },

    "gray": {
        "definition": "Gray is a neutral color between black and white.",
        "how_to_make": "Mix black and white to create gray. More white creates lighter gray, while more black creates darker gray."
    },

    "black": {
        "definition": "Black is a very dark neutral color commonly used for outlines, shadows, deep values, and strong contrast.",
        "how_to_make": "Black paint is usually easiest to use directly. Very dark mixtures can also be created by combining suitable deep colors."
    },

    "white": {
        "definition": "White is a light neutral color commonly used for highlights, mixing lighter colors, and creating tints.",
        "how_to_make": "White is generally used directly from white paint rather than being created by mixing basic paint colors."
    },

    "sunset": {
        "definition": "A sunset painting shows the sky and landscape during sunset using warm colors, changing light, silhouettes, and atmospheric effects.",
        "colors": "For a sunset, useful colors include yellow, orange, red, pink, purple, and blue. You can blend them gradually from lighter colors near the sun to deeper colors farther across the sky.",
        "how_to_make": "Start with yellow near the sun, blend into orange, then red or pink, and finally purple or blue toward the upper sky. Adjust the transitions gently.",
        "steps": "Paint the lightest area around the sun first. Add yellow, orange, pink, and red around it. Blend the colors gradually, then add purple or blue toward the upper sky. Finish with darker silhouettes for mountains, trees, buildings, or other objects.",
        "brushes": "Use a large flat brush for the sky, a soft or filbert brush for blending, and a smaller round brush for the sun and details.",
        "techniques": "Soft blending, layering, and silhouettes work especially well for sunset paintings.",
        "tips": "Keep the brightest area close to the sun and gradually make the surrounding sky darker. Avoid using too much black because it can make the sunset look muddy."
    },

    "sunset_colors": {
        "definition": "Sunset colors are warm and atmospheric colors used to represent the changing light of the sky.",
        "how_to_make": "Use yellow, orange, red, pink, purple, and blue. Mix neighboring colors gradually instead of creating harsh transitions.",
        "tips": "Use more yellow and orange near the sun and deeper red, purple, and blue farther away."
    },

    "trees": {
        "definition": "Trees can be painted using different greens, browns, yellows, blues, and darker tones depending on the lighting and artistic style.",
        "colors": "For natural trees, use several greens rather than one flat green. Mix green with yellow for lighter leaves, blue for cooler darker greens, and small amounts of brown for earthy tones.",
        "brushes": "Use a flat or filbert brush for the larger tree masses and a round or detail brush for branches, leaves, and small details.",
        "steps": "Start with the trunk and main branches. Add the large leaf shapes, then build lighter and darker green areas. Finish with small branches and selected leaf details.",
        "techniques": "Layering, dry brushing, dabbing, and stippling can create natural-looking foliage.",
        "tips": "Avoid making every leaf identical. Vary the size, shape, value, and direction of your marks."
    },

    "traditional_trees": {
        "definition": "Traditional-style tree painting usually focuses on natural-looking shapes, earthy colors, visible branches, and layered foliage.",
        "colors": "Use olive green, forest green, yellow-green, brown, ochre, and darker green. Add warm yellow or orange where sunlight hits the leaves.",
        "brushes": "Use a filbert or flat brush for foliage masses and a round brush for branches and smaller details.",
        "steps": "Paint the trunk and branches first, build the main foliage masses, add darker green shadows, then add lighter leaves and small details.",
        "tips": "Keep the colors natural and use lighter tones where the light reaches the tree."
    },

    "ghibli_trees": {
        "definition": "For a soft animated or storybook-inspired tree look, use simplified shapes, gentle color transitions, rounded foliage, and atmospheric lighting rather than trying to reproduce a specific artwork exactly.",
        "colors": "Try soft greens, olive green, yellow-green, muted blue-green, warm brown, cream, and gentle yellow highlights. For a dreamy scene, slightly desaturated colors can work well.",
        "brushes": "Use a large soft or filbert brush for rounded foliage, a flat brush for larger shapes, and a small round brush for branches and selected leaf details.",
        "steps": "Block in a simple rounded tree silhouette, add medium green foliage, place darker green areas underneath, then add warm light-green or yellow highlights. Keep some areas soft and simplified.",
        "techniques": "Soft blending, layering, simplified shapes, atmospheric perspective, and gentle highlights can create a storybook-inspired appearance.",
        "tips": "Focus on the overall mood and simplified shapes rather than painting every individual leaf."
    },

    "rocks": {
        "definition": "Rocks can be painted by building simple shapes with a base color, darker shadow areas, and lighter planes that show the direction of light.",
        "colors": "Useful rock colors include gray, brown, beige, muted green, blue-gray, and warm earth tones. Mix several related colors instead of using one flat gray.",
        "brushes": "Use a flat brush for broad rock planes, a round brush for cracks and smaller details, and a dry brush for rough texture.",
        "steps": "Sketch the rock shape, apply a base color, add darker shadow planes, add lighter areas facing the light, then add cracks and texture.",
        "techniques": "Dry brushing, layering, and broken brush strokes work well for rocky textures.",
        "tips": "Keep the light direction consistent so the rock looks three-dimensional."
    },

    "clouds": {
        "definition": "Clouds are soft atmospheric forms that can be painted using layered light and shadow shapes.",
        "colors": "Use white, light blue, gray, pale pink, lavender, yellow, or orange depending on the sky and lighting.",
        "brushes": "Use a soft round, filbert, or soft flat brush for cloud shapes and gentle blending.",
        "steps": "Block in the basic cloud shape, add lighter areas facing the light, place soft shadows underneath, and blend selected edges.",
        "tips": "Keep some edges soft and some edges clearer so the clouds do not look completely flat."
    },

    "mountains": {
        "definition": "Mountains can be painted using layered shapes, changes in value, and atmospheric perspective.",
        "colors": "Use blue, blue-gray, purple, brown, green, and lighter atmospheric colors depending on distance and lighting.",
        "brushes": "Flat brushes are useful for mountain planes, while smaller round brushes can add rock and snow details.",
        "steps": "Block in the distant mountains first, then add closer darker mountains. Add light-facing planes and selected details last.",
        "tips": "Distant mountains usually appear lighter and less detailed than foreground mountains."
    },

    "sky": {
        "definition": "The sky can be painted using large blended areas of color and gradual changes in value.",
        "colors": "Common sky colors include blue, cyan, white, pink, orange, yellow, purple, and gray depending on the weather and time of day.",
        "brushes": "Use large flat or soft brushes for broad sky areas and smaller brushes for clouds and details.",
        "techniques": "Blending, layering, wet-on-wet, and soft transitions are useful for skies."
    },

    "landscape": {
        "definition": "A landscape painting represents natural or outdoor scenery such as mountains, trees, rivers, skies, fields, and rocks.",
        "materials": "Useful materials include paints, several brush sizes, canvas or suitable paper, palette, water container, cloth, and a pencil for a light sketch.",
        "steps": "Plan the composition, sketch large shapes, paint the sky, establish distant objects, build the middle ground, add foreground details, and finish with highlights.",
        "tips": "Create depth by making distant objects lighter and less detailed and foreground objects stronger and more detailed."
    },

    "happy": {
        "feelings": "Painting can feel joyful and satisfying because it gives people an opportunity to create, experiment with colors, and express themselves.",
        "tips": "For a happier painting session, try bright colors, playful subjects, colorful patterns, flowers, landscapes, or anything that you personally enjoy creating."
    },

    "sad": {
        "feelings": "Painting can provide a creative way to express difficult emotions. Some people find it calming or comforting to put their feelings into colors and images.",
        "tips": "When you feel low, you can paint freely without worrying about making the artwork perfect. Focus on expressing yourself rather than judging the result."
    },

    "relaxation": {
        "feelings": "Painting can be a calming activity because it encourages focus on colors, shapes, brush movements, and the creative process.",
        "tips": "Try slow brush movements, simple subjects, gentle colors, and a comfortable environment when you want a more relaxing painting session."
    }
}

greeting_responses = {
    "greeting": (
        "Hello! 🎨 How can I help you with painting today?",
        "Hey! What would you like to know about painting?",
        "Hii! Ask me anything about paints, brushes, canvas, colors, or techniques!"
    ),

    "goodbye": (
        "Goodbye! Keep creating!",
        "See you later! 🎨",
        "Bye! Take care and happy painting!"
    )
}

def find_question_types(message):
    found_types = []

    for category in question_words:
        if category in ("greeting", "goodbye"):
            continue

        for phrase in question_words[category]:
            if phrase in message:
                if category not in found_types:
                    found_types.append(category)
                break

    return found_types

def find_topics(message):
    found_topics = []

    sorted_topics = sorted(
        painting_knowledge.keys(),
        key=len,
        reverse=True
    )

    for topic in sorted_topics:
        topic_name = topic.replace("_", " ")

        if topic in message or topic_name in message:
            if topic not in found_topics:
                found_topics.append(topic)

    return found_topics

def has_greeting(message):
    for phrase in question_words["greeting"]:
        if " " in phrase:
            if phrase in message:
                return True
        else:
            if phrase in message.split():
                return True

    return False

def has_goodbye(message):
    for phrase in question_words["goodbye"]:
        if " " in phrase:
            if phrase in message:
                return True
        else:
            if phrase in message.split():
                return True

    return False

def find_special_answers(message):
    special_responses = []

    if "sunset" in message:
        if any(word in message for word in ["make", "paint", "create", "draw"]):
            special_responses.append(painting_knowledge["sunset"]["how_to_make"])
        elif "brush" in message:
            special_responses.append(painting_knowledge["sunset"]["brushes"])
        elif "color" in message or "colour" in message:
            special_responses.append(painting_knowledge["sunset"]["colors"])
        elif "step" in message or "process" in message:
            special_responses.append(painting_knowledge["sunset"]["steps"])

    if "tree" in message or "trees" in message:
        if "ghibli" in message or "anime" in message or "storybook" in message:
            if "color" in message or "colour" in message:
                special_responses.append(painting_knowledge["ghibli_trees"]["colors"])
            elif "brush" in message:
                special_responses.append(painting_knowledge["ghibli_trees"]["brushes"])
            elif "step" in message or "paint" in message or "make" in message:
                special_responses.append(painting_knowledge["ghibli_trees"]["steps"])
            else:
                special_responses.append(painting_knowledge["ghibli_trees"]["definition"])
        elif "traditional" in message:
            if "color" in message or "colour" in message:
                special_responses.append(painting_knowledge["traditional_trees"]["colors"])
            elif "brush" in message:
                special_responses.append(painting_knowledge["traditional_trees"]["brushes"])
            elif "step" in message or "paint" in message or "make" in message:
                special_responses.append(painting_knowledge["traditional_trees"]["steps"])
            else:
                special_responses.append(painting_knowledge["traditional_trees"]["definition"])

    if "rock" in message or "rocks" in message:
        if "brush" in message:
            special_responses.append(painting_knowledge["rocks"]["brushes"])
        elif "color" in message or "colour" in message:
            special_responses.append(painting_knowledge["rocks"]["colors"])
        elif "step" in message or "paint" in message or "make" in message:
            special_responses.append(painting_knowledge["rocks"]["steps"])

    if "cloud" in message or "clouds" in message:
        if "brush" in message:
            special_responses.append(painting_knowledge["clouds"]["brushes"])
        elif "color" in message or "colour" in message:
            special_responses.append(painting_knowledge["clouds"]["colors"])
        elif "step" in message or "paint" in message or "make" in message:
            special_responses.append(painting_knowledge["clouds"]["steps"])

    if "mountain" in message or "mountains" in message:
        if "brush" in message:
            special_responses.append(painting_knowledge["mountains"]["brushes"])
        elif "color" in message or "colour" in message:
            special_responses.append(painting_knowledge["mountains"]["colors"])
        elif "step" in message or "paint" in message or "make" in message:
            special_responses.append(painting_knowledge["mountains"]["steps"])

    return special_responses

@app.route("/chat", methods=["POST"])
def chat():

    print("chat is responding")

    data = request.json

    if not data or "message" not in data:
        return ["Please enter a message."]

    message = data["message"].lower().strip()

    responses = []

    question_types = find_question_types(message)
    topics = find_topics(message)

    if has_greeting(message):
        responses.append(
            greeting_responses["greeting"][0]
        )

    if has_goodbye(message):
        responses.append(
            greeting_responses["goodbye"][0]
        )

    special_answers = find_special_answers(message)

    for answer in special_answers:
        if answer not in responses:
            responses.append(answer)

    if topics:

        for topic in topics:

            topic_data = painting_knowledge[topic]

            topic_responses = []

            if question_types:

                for question_type in question_types:

                    if question_type in topic_data:

                        answer = topic_data[question_type]

                        if isinstance(answer, str):
                            topic_responses.append(answer)

            if not topic_responses:

                if "definition" in topic_data:
                    topic_responses.append(
                        topic_data["definition"]
                    )

            for answer in topic_responses:

                if answer not in responses:
                    responses.append(answer)

    if not responses:

        responses.append(
            "Sorry, I don't understand that yet. 🎨 "
            "Try asking me about painting, paints, colors, "
            "brushes, canvas, techniques, sunsets, trees, "
            "rocks, clouds, mountains, or landscapes."
        )

    return responses

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

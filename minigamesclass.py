# -*- coding: utf-8 -*-
import config
from config import *
from database import getPoints, addPoints
from random import choice


class minigames(object):
    def __init__(self, bot):
        super().__init__()
        self.gamenameurls = {
            "Airhockey": "https://cdn.discordapp.com/attachments/701015289374179348/735513911021010964/tutorial_airhockey.png"
            ,
            "Amnesia": "https://cdn.discordapp.com/attachments/701015289374179348/735514256107241523/tutorial_amnesia.png"
            ,
            "Anaconda": "https://cdn.discordapp.com/attachments/701015289374179348/735514443810865182/tutorial_anaconda.png"
            , "Balls": "https://cdn.discordapp.com/attachments/701015289374179348/735514453331673160/tutorial_balls.png"
            ,
            "Banarama": "https://cdn.discordapp.com/attachments/701015289374179348/735514883700817940/tutorial_bananarama.png"
            ,
            "Beckham": "https://cdn.discordapp.com/attachments/701015289374179348/735514952952971294/tutorial_beckham.png"
            ,
            "Belfry": "https://cdn.discordapp.com/attachments/701015289374179348/735515032888279130/tutorial_belfry.png"
            ,
            "Blocky": "https://cdn.discordapp.com/attachments/701015289374179348/735515044103847946/tutorial_blocky.png"
            ,
            "Bounce": "https://cdn.discordapp.com/attachments/701015289374179348/735515079008845980/tutorial_bounce.png"
            ,
            "Bubble": "https://cdn.discordapp.com/attachments/701015289374179348/735515292746383450/tutorial_bubble.png"
            ,
            "Catena": "https://cdn.discordapp.com/attachments/701015289374179348/735515529632022568/tutorial_catena.png"
            , "Chop": "https://cdn.discordapp.com/attachments/701015289374179348/735515608413896804/tutorial_chop.png"
            ,
            "Coulours": "https://cdn.discordapp.com/attachments/701015289374179348/735515634279907389/tutorial_colours.png"
            , "Cup": "https://cdn.discordapp.com/attachments/701015289374179348/735515680077512714/tutorial_cup.png"
            , "Dodge": "https://cdn.discordapp.com/attachments/701015289374179348/735515760046375059/tutorial_dodge.png"
            , "Dots": "https://cdn.discordapp.com/attachments/701015289374179348/735515764437680178/tutorial_dots.png"
            ,
            "Double": "https://cdn.discordapp.com/attachments/701015289374179348/735515769110265896/tutorial_double.png"
            , "Drop": "https://cdn.discordapp.com/attachments/701015289374179348/735515779050504322/tutorial_drop.png"
            , "Dunk": "https://cdn.discordapp.com/attachments/701015289374179348/735515789662355577/tutorial_dunk.png"
            , "Equal": "https://cdn.discordapp.com/attachments/701015289374179348/735515789662355577/tutorial_dunk.png"
            ,
            "Frappe": "https://cdn.discordapp.com/attachments/701015289374179348/735515983388868668/tutorial_frappe.png"
            ,
            "Freedom": "https://cdn.discordapp.com/attachments/701015289374179348/735515991999774740/tutorial_freedom.png"
            , "Go": "https://cdn.discordapp.com/attachments/701015289374179348/735516036627169300/tutorial_go.png"
            , "Grace": "https://cdn.discordapp.com/attachments/701015289374179348/735516038380126208/tutorial_grace.png"
            ,
            "Harpun": "https://cdn.discordapp.com/attachments/701015289374179348/735516040867479582/tutorial_harpun.png"
            ,
            "Hockey": "https://cdn.discordapp.com/attachments/701015289374179348/735516138401693776/tutorial_hockey.png"
            ,
            "Hunted": "https://cdn.discordapp.com/attachments/701015289374179348/735516140112969728/tutorial_hunted.png"
            ,
            "Impossible": "https://cdn.discordapp.com/attachments/701015289374179348/735516143984443472/tutorial_impossible.png"
            , "Jelly": "https://cdn.discordapp.com/attachments/701015289374179348/735516148061307000/tutorial_jelly.png"
            ,
            "Jordan": "https://cdn.discordapp.com/attachments/701015289374179348/735516150695329853/tutorial_jordan.png"
            , "Knock": "https://cdn.discordapp.com/attachments/701015289374179348/735516154168344716/tutorial_knock.png"
            , "Kobe": "https://cdn.discordapp.com/attachments/701015289374179348/735516156978397284/tutorial_kobe.png"
            ,
            "Machete": "https://cdn.discordapp.com/attachments/701015289374179348/735516162519203840/tutorial_machete.png"
            ,
            "Numbree": "https://cdn.discordapp.com/attachments/701015289374179348/735516618783981640/tutorial_numbree.png"
            , "Plick": "https://cdn.discordapp.com/attachments/701015289374179348/735516620277022901/tutorial_plick.png"
            , "Puck": "https://cdn.discordapp.com/attachments/701015289374179348/735516621279592478/tutorial_puck.png"
            ,
            "Ravine": "https://cdn.discordapp.com/attachments/701015289374179348/735516623259172884/tutorial_ravine.png"
            ,
            "Rockety": "https://cdn.discordapp.com/attachments/701015289374179348/735516723503169606/tutorial_rockety.png"
            ,
            "Rolandz": "https://cdn.discordapp.com/attachments/701015289374179348/735516725256388648/tutorial_rolandz.png"
            ,
            "Satellite": "https://cdn.discordapp.com/attachments/701015289374179348/735516727391289444/tutorial_satellite.png"
            ,
            "Snatch": "https://cdn.discordapp.com/attachments/701015289374179348/735516734265622598/tutorial_snatch.png"
            , "Swace": "https://cdn.discordapp.com/attachments/701015289374179348/735517179167899678/tutorial_swace.png"
            ,
            "Tarzan": "https://cdn.discordapp.com/attachments/701015289374179348/735517185350434986/tutorial_tarzan.png"
            ,
            "Torpedo": "https://cdn.discordapp.com/attachments/701015289374179348/735517187061710888/tutorial_torpedo.png"
            ,
            "Twister": "https://cdn.discordapp.com/attachments/701015289374179348/735517189972557954/tutorial_twister.png"
            , "UFO": "https://cdn.discordapp.com/attachments/701015289374179348/735517196217876590/tutorial_ufo.png"
            ,
            "Zidane": "https://cdn.discordapp.com/attachments/701015289374179348/735517200902783077/tutorial_zidane.png"
            ,
            "Baller": "https://cdn.discordapp.com/attachments/701015289374179348/735536798452678748/tutorial_baller.png"
            ,
            "Capriole": "https://cdn.discordapp.com/attachments/701015289374179348/735536817536892928/tutorial_capriole.png"
            ,
            "Dribble": "https://cdn.discordapp.com/attachments/701015289374179348/735536833709998090/tutorial_dribble.png"
            ,
            "Fotbolt": "https://cdn.discordapp.com/attachments/701015289374179348/735536850772426752/tutorial_fotbolt.png"
            , "Hoop": "https://cdn.discordapp.com/attachments/701015289374179348/735536880061251714/tutorial_hoop.png"
            , "Ingot": "https://cdn.discordapp.com/attachments/701015289374179348/735536896264110130/tutorial_ingot.png"
            ,
            "Jellytwo": "https://cdn.discordapp.com/attachments/701015289374179348/735536908113019011/tutorial_jellytwo.png"
            ,
            "Jumpers": "https://cdn.discordapp.com/attachments/701015289374179348/735536917579431996/tutorial_jumpers.png"
            ,
            "Landing": "https://cdn.discordapp.com/attachments/701015289374179348/735536963041492992/tutorial_landing.png"
            ,
            "Pinger": "https://cdn.discordapp.com/attachments/701015289374179348/735536976094036048/tutorial_pinger.png"
            ,
            "Planet": "https://cdn.discordapp.com/attachments/701015289374179348/735536986978254908/tutorial_planet.png"
            ,
            "Platform": "https://cdn.discordapp.com/attachments/701015289374179348/735536998005211136/tutorial_platform.png"
            , "Pong": "https://cdn.discordapp.com/attachments/701015289374179348/735537007102787714/tutorial_pong.png"
            , "Pool": "https://cdn.discordapp.com/attachments/701015289374179348/735537016770527232/tutorial_pool.png"
            , "Rings": "https://cdn.discordapp.com/attachments/701015289374179348/735537027432316978/tutorial_rings.png"
            ,
            "Shapes": "https://cdn.discordapp.com/attachments/701015289374179348/735537038757199992/tutorial_shapes.png"
            ,
            "Sidewinder": "https://cdn.discordapp.com/attachments/701015289374179348/735537045597847562/tutorial_sidewinder.png"
            , "Slope": "https://cdn.discordapp.com/attachments/701015289374179348/735537075343851590/tutorial_slope.png"
            ,
            "Trails": "https://cdn.discordapp.com/attachments/701015289374179348/735539835896594462/tutorial_trails.png"
            , "Whack": "https://cdn.discordapp.com/attachments/701015289374179348/735537101642399864/tutorial_whack.png"
            ,
            "Wheelie": "https://cdn.discordapp.com/attachments/701015289374179348/735537109854715912/tutorial_wheelie.png"
            ,
            "Zeemon": "https://cdn.discordapp.com/attachments/701015289374179348/735537118415421520/tutorial_zeemon.png"
        }
        self.gamenamegames = [
            "Airhockey", "Amnesia", "Anaconda",
            "Balls", "Banarama", "Beckham", "Belfry", "Blocky", "Bounce", "Bubble", "Catena", "Chop",
            "Coulours", "Cup", "Dodge", "Dots", "Double", "Drop", "Dunk", "Equal", "Frappe", "Freedom", "Go",
            "Grace", "Harpun", "Hockey", "Hunted", "Impossible", "Jelly", "Jordan", "Knock", "Kobe", "Machete",
            "Numbree", "Plick", "Puck", "Ravine", "Rockety", "Rolandz", "Satellite",
            "Snatch", "Swace", "Tarzan", "Torpedo", "Twister", "UFO", "Zidane", "Baller", "Capriole", "Dribble",
            "Fotbolt", "Hoop", "Ingot", "Jellytwo", "Jumpers", "Landing", "Pinger", "Planet", "Platform",
            "Pong", "Pool", "Rings", "Shapes", "Sidewinder", "Slope", "Trails", "Whack", "Wheelie", "Zeemon"]
        self.ongoing = False
        self.minigames = [
            self.unscramble, self.hangman, self.equation, self.equal, self.capital, self.flags, self.gamename
        ]
        self.bot = bot
        self.price = ""
        self.flariegames = ['Airhockey', 'Amnesia', 'Anaconda', 'Baller', 'Balls', 'Banarama', 'Beckham', 'Belfry',
                            'Blocky', 'Bounce', 'Bubble', 'Capriole', 'Catena', 'Chop', 'Colours', 'Cup', 'Dodge',
                            'Dots',
                            'Double', 'Dribble', 'Drop', 'Dunk', 'Equal', 'Fotbolt', 'Frappe', 'Freedom', 'Go', 'Grace',
                            'Harpun', 'Hockey', 'Hoop', 'Hunted', 'Impossible', 'Ingot', 'Jelly', 'Jelly2', 'Jordan',
                            'Jumpers', 'Knock', 'Kobe', 'Landing', 'Machete', 'Numbree', 'Pinger', 'Planet', 'Platform',
                            'Plick', 'Pong', 'Pool', 'Puck', 'Ravine', 'Rings', 'Rockety', 'Rolandz', 'Satellite',
                            'Shapes',
                            'Sidewinder', 'Slope', 'Snatch', 'Swace', 'Tarzan', 'Torpedo', 'Trails', 'Twister', 'UFO',
                            'Whack', 'Wheelie', 'Zeemon', 'Zidane']
        self.wordlist = ['hover', 'curly', 'nine', 'observation', 'tease', 'vest', 'finicky', 'smile', 'brother',
                         'overrated', 'gate', 'bathe', 'consist', 'afraid', 'partner', 'territory', 'satisfying',
                         'simplistic', 'legs', 'silk', 'cast', 'keen', 'zebra', 'moldy', 'scratch', 'screw',
                         'questionable', 'welcome', 'fork', 'nervous', 'fax', 'kittens', 'transport', 'sharp', 'bitter',
                         'sort', 'wealthy', 'class', 'juvenile', 'abandoned', 'disastrous', 'fragile', 'company',
                         'pause',
                         'tough', 'superficial', 'basketball', 'coil', 'solid', 'hurried', 'rabbit', 'concern', 'star',
                         'dress', 'tranquil', 'beg', 'hideous', 'imaginary', 'bubble', 'flagrant', 'cook', 'breakable',
                         'boil', 'spooky', 'youthful', 'show', 'cable', 'comparison', 'horses', 'step', 'profuse',
                         'muddle', 'fireman', 'wall', 'treat', 'fish', 'calm', 'attempt', 'cherries', 'search', 'allow',
                         'accidental', 'sponge', 'proud', 'chunky', 'wait', 'spiders', 'remember', 'instinctive',
                         'burst',
                         'courageous', 'annoying', 'ready', 'helpless', 'flag', 'unknown', 'found', 'brick', 'contain',
                         'jam', 'common', 'connection', 'stormy', 'obtainable', 'filthy', 'force', 'wiry', 'dislike',
                         'luxuriant', 'tall', 'ear', 'apologise', 'fang', 'excited', 'grieving', 'rightful', 'teaching',
                         'rabbits', 'crash', 'verdant', 'magenta', 'paper', 'hate', 'fuel', 'frighten', 'industry',
                         'attraction', 'rinse', 'mix', 'month', 'scarecrow', 'downtown', 'clam', 'chew', 'smoggy',
                         'recondite', 'bad', 'word', 'join', 'coordinated', 'happen', 'avoid', 'endurable', 'sofa',
                         'wise',
                         'habitual', 'dazzling', 'jeans', 'next', 'empty', 'sparkling', 'aback', 'island', 'approval',
                         'horse', 'quickest', 'future', 'able', 'advise', 'fine', 'smiling', 'resonant', 'lacking',
                         'rifle', 'sleep', 'tense', 'elite', 'pastoral', 'finger', 'swift', 'lighten', 'fortunate',
                         'scrub', 'market', 'rhetorical', 'meal', 'cure', 'orange', 'beef', 'flame', 'roasted',
                         'terrific',
                         'cub', 'defective', 'naive', 'float', 'pancake', 'statement', 'chalk', 'trap', 'homely',
                         'doctor',
                         'pushy', 'simple', 'library', 'cemetery', 'shut', 'charming', 'combative', 'grumpy', 'manage',
                         'hysterical', 'wonderful', 'boat', 'wail', 'mindless', 'madly', 'confess', 'position', 'brave',
                         'hover', 'health', 'pat', 'venomous', 'dirt', 'umbrella', 'anxious', 'amusement', 'sweater',
                         'alive', 'flowery', 'basket', 'quarter', 'powerful', 'duck', 'pause', 'oven', 'lace', 'toy',
                         'naughty', 'shocking', 'damaged', 'lip', 'interrupt', 'callous', 'elfin', 'blue-eyed',
                         'believe',
                         'grease', 'absent', 'muddled', 'encourage', 'cuddly', 'simple', 'husky', 'telephone',
                         'fireman',
                         'aberrant', 'annoying', 'tedious', 'squealing', 'slippery', 'drain', 'acidic', 'ten', 'own',
                         'return', 'real', 'bouncy', 'lackadaisical', 'curve', 'grain', 'file', 'welcome', 'meaty',
                         'strong', 'bird', 'moan', 'adjustment', 'dream', 'freezing', 'base', 'dear', 'tax', 'pinch',
                         'straw', 'wrestle', 'tightfisted', 'abundant', 'groan', 'stormy', 'lovely', 'concern',
                         'picayune',
                         'smelly', 'vacation', 'wealth', 'tramp', 'thunder', 'prefer', 'note', 'tray', 'guiltless',
                         'pointless', 'inquisitive', 'belligerent', 'female', 'car', 'roof', 'stingy', 'productive',
                         'unbiased', 'complex', 'resonant', 'nest', 'harsh', 'leg', 'spill', 'plan', 'plough', 'wire',
                         'boast', 'yielding', 'lazy', 'support', 'laughable', 'magenta', 'handle', 'obedient', 'bent',
                         'abortive', 'periodic', 'earn', 'spiffy', 'purpose', 'suck', 'current', 'men', 'request',
                         'stitch', 'coherent', 'dime', 'rainy', 'curl', 'knowing', 'glass', 'afterthought', 'happen',
                         'blind', 'sense', 'order', 'mom', 'prepare', 'surround', 'tall', 'education', 'lamentable',
                         'exotic', 'accessible', 'snatch', 'mate', 'grumpy', 'suspect', 'mushy', 'flap', 'possible',
                         'hour', 'spark', 'reply', 'organic', 'silver', 'full', 'wrathful', 'please', 'ducks', 'ajar',
                         'report', 'crabby', 'watch', 'guttural', 'statuesque', 'decay', 'quizzical', 'carpenter',
                         'command', 'probable', 'disgusting', 'able', 'drum', 'van', 'imagine', 'program', 'four',
                         'flood',
                         'live', 'grandmother', 'big', 'scandalous', 'deliver', 'ignore', 'voiceless', 'instruct',
                         'fit',
                         'existence', 'vase', 'needy', 'snail', 'receipt', 'jeans', 'search', 'hard-to-find', 'better',
                         'plant', 'shape', 'skin', 'sharp', 'groovy', 'land', 'satisfying', 'cub', 'metal', 'vest',
                         'idiotic', 'marry', 'voracious', 'cross', 'float', 'tank', 'motion', 'fade', 'eatable',
                         'deranged', 'instinctive', 'rock', 'chase', 'beds', 'bathe', 'clammy', 'act', 'cook', 'pale',
                         'bruise', 'spray', 'magic', 'temper', 'lowly', 'buzz', 'chicken', 'copper', 'touch', 'chief',
                         'utter', 'endurable', 'noiseless', 'yellow', 'birthday', 'round', 'bang', 'ill', 'scrub',
                         'butter', 'actually', 'many', 'clip', 'young', 'charming', 'towering', 'society', 'close',
                         'found', 'deeply', 'cagey', 'bikes', 'distance', 'stream', 'humor', 'cemetery', 'sponge',
                         'important', 'tie', 'scare', 'bell', 'continue', 'powder', 'wish', 'smoke', 'thin', 'tacky',
                         'desire', 'deadpan', 'settle', 'uneven', 'preach', 'hall', 'understood', 'scarecrow',
                         'elastic',
                         'tricky', 'mysterious', 'camp', 'unique', 'doubt', 'hungry', 'hapless', 'time', 'produce',
                         'bumpy', 'winter', 'knee', 'serious', 'onerous', 'calculate', 'huge', 'mist', 'save',
                         'spiders',
                         'quince', 'hug', 'direful', 'weather', 'deserted', 'joke', 'foamy', 'demonic', 'guess',
                         'offend',
                         'loving', 'unable', 'fold', 'correct', 'unfasten', 'elegant', 'tangy', 'relax', 'balance',
                         'nippy', 'discreet', 'bridge', 'tasteless', 'hollow', 'tremendous', 'modern', 'ugliest',
                         'trouble', 'notebook', 'familiar', 'plants', 'hypnotic', 'discover', 'ubiquitous', 'tin',
                         'workable', 'synonymous', 'assorted', 'possessive', 'rebel', 'spiky', 'experience', 'green',
                         'trade', 'daffy', 'wriggle', 'obsequious', 'expand', 'barbarous', 'ring', 'pink', 'exclusive',
                         'scarce', 'bottle', 'bewildered', 'outrageous', 'group', 'steam', 'quaint', 'plucky', 'public',
                         'reign', 'wax', 'early', 'careful', 'paper', 'value', 'waggish', 'effect', 'overrated',
                         'polite',
                         'lacking', 'mass', 'driving', 'jealous', 'mixed', 'harmony', 'belief', 'planes', 'interesting',
                         'tumble', 'righteous', 'giant', 'ossified', 'cheap', 'weight', 'chew', 'number', 'fantastic',
                         'calm', 'red', 'lucky', 'trace', 'spotless', 'lying', 'malicious', 'pack', 'star', 'comb',
                         'carry', 'puzzled', 'loutish', 'violent', 'ethereal', 'force', 'swanky', 'dazzling',
                         'blushing',
                         'tender', 'instrument', 'adjoining', 'dinosaurs', 'explode', 'heartbreaking', 'efficacious',
                         'wary', 'marble', 'maniacal', 'borrow', 'educated', 'mine', 'pet', 'racial', 'tiresome',
                         'domineering', 'weigh', 'quirky', 'cow', 'knot', 'increase', 'locket', 'grade', 'nutty',
                         'pipe',
                         'quickest', 'noxious', 'saw', 'comparison', 'rifle', 'seat', 'stem', 'letter', 'weak',
                         'dangerous', 'throne', 'wing', 'feeble', 'analyse', 'key', 'field', 'amused', 'unit', 'plate',
                         'observe', 'divergent', 'baby', 'channel', 'brown', 'actor', 'drab', 'haunt', 'merciful',
                         'private', 'wakeful', 'friends', 'part', 'sparkle', 'view', 'mind', 'button', 'impress',
                         'strange', 'resolute', 'dance', 'charge', 'fresh', 'accept', 'hydrant', 'step', 'cap', 'tiger',
                         'long', 'honey', 'material', 'numerous', 'intelligent', 'bump', 'aunt', 'attach', 'peck',
                         'ruin',
                         'confuse', 'aromatic', 'thankful', 'border', 'wheel', 'craven', 'wait', 'morning', 'high',
                         'murder', 'chunky', 'look', 'uppity', 'testy', 'subdued', 'used', 'wise', 'obtainable',
                         'naive',
                         'smoggy', 'aboard', 'concerned', 'jagged', 'woebegone', 'page', 'decisive', 'capricious',
                         'office', 'peaceful', 'brush', 'silly', 'license', 'arrogant', 'sniff', 'cars', 'loose',
                         'bedroom', 'pumped', 'warn', 'theory', 'farm', 'nation', 'collar', 'guarded', 'free',
                         'futuristic', 'rub', 'didactic', 'absurd', 'pedal', 'division', 'wall', 'skip', 'minor',
                         'well-made', 'cable', 'whimsical', 'dog', 'dull', 'fascinated', 'vengeful', 'odd', 'work',
                         'interfere', 'plug', 'agreement', 'grab', 'abandoned', 'depressed', 'broken', 'development',
                         'nifty', 'inform', 'zoom', 'broad', 'porter', 'double', 'range', 'object', 'innate', 'thumb',
                         'scribble', 'rot', 'insect', 'dashing', 'troubled', 'stranger', 'include', 'abrasive', 'half',
                         'unite', 'silky', 'secretive', 'disagreeable', 'adorable', 'kind', 'acrid', 'bulb', 'offbeat',
                         'dinner', 'hushed', 'standing', 'mammoth', 'woman', 'secret', 'reproduce', 'allow', 'wrench',
                         'labored', 'scold', 'nut', 'concentrate', 'stereotyped', 'nebulous', 'brick', 'icy', 'glue',
                         'mark', 'irate', 'helpful', 'vigorous', 'attend', 'homely', 'poison', 'account', 'lie',
                         'judicious', 'statement', 'room', 'vessel', 'romantic', 'mere', 'worthless', 'reading', 'bike',
                         'hobbies', 'second-hand', 'list', 'sheep', 'wiggly', 'squeamish', 'cherries', 'suffer',
                         'grass',
                         'tap', 'spot', 'brake', 'billowy', 'toe', 'miscreant', 'books', 'scatter', 'crayon', 'way',
                         'squash', 'turn', 'cruel', 'cloudy', 'aspiring', 'glorious', 'faint', 'month', 'pretend',
                         'evasive', 'quiver', 'responsible', 'rigid', 'dirty', 'undress', 'pushy', 'deep', 'visitor',
                         'desert', 'finicky', 'colorful', 'summer', 'ritzy', 'back', 'smooth', 'smile', 'bushes',
                         'humorous', 'abstracted', 'spy', 'add', 'girls', 'jumpy', 'short', 'debt', 'makeshift', 'nod',
                         'poke', 'enormous', 'dizzy', 'mountain', 'sleepy', 'help', 'shoes', 'redundant', 'mice',
                         'joyous',
                         'letters', 'stocking', 'bee', 'inexpensive', 'test', 'passenger', 'crooked', 'prevent',
                         'gigantic', 'lamp', 'bat', 'cycle', 'pop', 'property', 'disapprove', 'dark', 'prickly',
                         'meeting',
                         'feeling', 'frighten', 'trick', 'unsuitable', 'acoustic', 'vagabond', 'aloof', 'yummy',
                         'bright',
                         'women', 'juice', 'grandfather', 'third', 'bitter', 'kneel', 'coach', 'flashy', 'delight',
                         'low',
                         'hallowed', 'lyrical', 'limit', 'flawless', 'curly', 'flagrant', 'ultra', 'frail', 'end',
                         'attract', 'left', 'worm', 'basin', 'gold', 'fluffy', 'high-pitched', 'bath', 'forgetful',
                         'elite', 'frog', 'escape', 'cheer', 'exultant', 'motionless', 'club', 'bolt', 'wacky', 'carve',
                         'goofy', 'sail', 'amount', 'debonair', 'unused', 'fail', 'ignorant', 'well-to-do', 'tight',
                         'medical', 'gratis', 'boring', 'grin', 'blow', 'friendly', 'possess', 'miss', 'partner',
                         'kaput',
                         'wren', 'advice', 'succeed', 'island', 'songs', 'uninterested', 'combative', 'mean', 'load',
                         'whole', 'knowledgeable', 'comfortable', 'detect', 'cabbage', 'slope', 'bake', 'historical',
                         'frightened', 'courageous', 'foregoing', 'somber', 'apparatus', 'creepy', 'carriage', 'mask',
                         'unruly', 'lewd', 'digestion', 'stir', 'rhetorical', 'writer', 'hanging', 'waiting', 'drown',
                         'cup', 'fat', 'quicksand', 'gamy', 'pleasure', 'war', 'distinct', 'unarmed', 'paltry', 'sock',
                         'tour', 'crown', 'corn', 'unnatural', 'fluttering', 'cellar', 'pin', 'bait', 'abashed',
                         'curious',
                         'aftermath', 'teeny', 'plausible', 'monkey', 'tired', 'condition', 'rapid', 'teaching',
                         'stove',
                         'filthy', 'heavy', 'sink', 'occur', 'example', 'overjoyed', 'ship', 'run', 'oceanic',
                         'attempt',
                         'extra-large', 'elated', 'ceaseless', 'need', 'home', 'launch', 'dare', 'raise', 'moldy',
                         'floor',
                         'afternoon', 'alleged', 'ill-fated', 'fabulous', 'sedate', 'peep', 'crawl', 'shelf', 'flash',
                         'fang', 'outgoing', 'abiding', 'regret', 'cynical', 'pest', 'wave', 'maddening', 'skillful',
                         'arch', 'preserve', 'easy', 'bustling', 'doubtful', 'illustrious', 'youthful', 'gabby',
                         'bawdy',
                         'sticky', 'orange', 'loaf', 'drawer', 'answer', 'electric', 'destroy', 'quick', 'identify',
                         'necessary', 'horse', 'birds', 'plastic', 'rejoice', 'ski', 'stiff', 'judge', 'trousers',
                         'repeat', 'church', 'eyes', 'nondescript', 'bubble', 'son', 'gruesome', 'bone', 'x-ray',
                         'cloistered', 'dreary', 'cave', 'complain', 'regular', 'ray', 'earthquake', 'questionable',
                         'axiomatic', 'admit', 'cumbersome', 'influence', 'stage', 'various', 'country', 'puncture',
                         'boorish', 'military', 'cowardly', 'hope', 'wooden', 'agonizing', 'melodic', 'curved',
                         'incompetent', 'crate', 'mother', 'squeeze', 'pig', 'cooing', 'observant', 'earsplitting',
                         'sound', 'draconian', 'soak', 'disarm', 'detail', 'grieving', 'harass', 'substance',
                         'painstaking', 'honorable', 'shake', 'gullible', 'phone', 'action', 'scissors', 'enjoy',
                         'overconfident', 'vegetable', 'separate', 'thread', 'macho', 'educate', 'healthy', 'wood',
                         'nauseating', 'depend', 'delicious', 'polish', 'airplane', 'immense', 'telling', 'ants',
                         'destruction', 'form', 'bells', 'great', 'can', 'typical', 'meat', 'punish', 'power', 'jump',
                         'transport', 'hideous', 'contain', 'trap', 'learn', 'extend', 'zippy']
        self.pris = ""
        self.ordet = ""

        async def minigametasktask(self):
            self.bot.loop.create_task(self.minigameschedule())

        @bot.event
        async def on_ready():
            await minigametasktask(self)

    async def minigameschedule(self):
        while not self.bot.is_closed():
            ingamespel = randint(0, len(self.flariegames) - 1)
            await self.bot.change_presence(activity=discord.Game(self.flariegames[ingamespel]))
            waitforgame = randint(1800, 3600)
            await sleep(waitforgame)
            self.pris = f"{config.minigamepris} Flarie Tokens"
            randomminigame = randint(0, int(len(self.minigames) - 1))
            chosengame = self.minigames[randomminigame]
            flariechannel = self.bot.get_channel(config.flariechannelid)
            await chosengame(flariechannel, self.pris)

    async def handlewin(self, message):
        if str(message.content).upper() == str(self.ordet).upper() and self.ongoing is True:
            self.ongoing = False
            await addPoints(message.author.id, "ft", config.minigamepris)
            await self.bot.get_channel(config.flariechannelid).send(
                f"Congrats <@{message.author.id}>! you won {self.price}! :tada:")

    async def unscramble(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            wordlistlength = (len(self.wordlist) - 1)
            randomword = randint(0, wordlistlength)
            self.ordet = self.wordlist[randomword]
            letters = list(self.ordet)
            shuffle(letters)
            embed = discord.Embed(title="What is the word?", description=" ".join(letters))
            embed.add_field(name=f"Winner gets {price}", value="Good luck!")
            embed.color = config.minigamescolour
            msg = await message.send(embed=embed)
            while self.ongoing:
                await sleep(3)
                shuffle(letters)
                embedd = discord.Embed(title="What is the word?", description=" ".join(letters))
                embedd.add_field(name=f"Winner gets {price}", value="Good luck!")
                embedd.color = discord.Color(15733703)
                await msg.edit(embed=embedd)
        else:
            await message.send("Minigame already ongoing")

    async def hangman(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            randomword = randint(0, len(self.wordlist) - 1)
            self.ordet = self.wordlist[randomword]
            shownletters = []
            while self.ongoing:
                foundhiddenletter = False
                while self.ongoing and not foundhiddenletter:
                    letter = randint(0, len(self.ordet) - 1)
                    if letter not in shownletters:
                        foundhiddenletter = True
                shownletters.append(letter)
                shownmessage = ""
                for i in range(len(self.ordet)):
                    if i in shownletters:
                        shownmessage += self.ordet[i]
                    else:
                        shownmessage += " _ "
                embed = discord.Embed(title="What is the word?", description=f"`{shownmessage}`")
                embed.add_field(name=f"Winner gets {price}", value="Good luck!")
                embed.color = config.minigamescolour
                if len(shownletters) == 1:
                    msg = await message.send(embed=embed)
                elif len(shownletters) > 1:
                    await msg.edit(embed=embed)
                    if len(shownletters) == len(self.ordet):
                        return
                await sleep(5)
        else:
            await message.send("Minigame already ongoing")

    async def equal(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            o = randint(0, 100)
            t = randint(0, 100)
            arithmetics = ["+", "*"]
            s = arithmetics[randint(0, 1)]
            if s == "+":
                self.ordet = o + t
            elif s == "*":
                self.ordet = o * t
            embed = discord.Embed(title="What does this equal?", description=f"{o}{s}{t}")
            embed.add_field(name=f"Winner gets {price}", value="Good luck!")
            embed.color = config.minigamescolour
            await message.send(embed=embed)
        else:
            await message.send("Minigame already ongoing")

    async def equation(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            a = randint(10, 98)
            b = randint(20, 196)
            c = randint(10, 98)
            d = randint(20, 196)
            e = randint(10, 98)
            f = randint(20, 196)
            self.ordet = b + d + f - a - c - e
            embed = discord.Embed(title="What is  :x:?",
                                  description=f"{a} + :pig: = {b}\n{c} + :apple: = {d}\n{e} + :baseball: = {f}\n:pig: + :apple: + :baseball: = :x:")
            embed.add_field(name=f"Winner gets {price}!", value="Good luck!")
            embed.color = config.minigamescolour
            await message.send(embed=embed)
        else:
            await message.send("Minigame already ongoing")

    async def capital(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            countries = {'Algeria': 'Algiers', 'Angola': 'Luanda', 'Botswana': 'Gaborone', 'Egypt': 'Cairo', 'Gambia': 'Banjul',
             'Ghana': 'Accra', 'Guinea': 'Conakry', 'Cameroon': 'Yaounde', 'Kenya': 'Nairobi', 'Congo': 'Kinshasa',
             'Libya': 'Tripoli', 'Madagascar': 'Antananarivo', 'Morocco': 'Rabat', 'Niger': 'Niamey',
             'Namibia': 'Windhoek', 'Nigeria': 'Abuja', 'Rwanda': 'Kigali', 'Somalia': 'Mogadishu', 'Tunisia': 'Tunis',
             'Uganda': 'Kampala', 'Zimbabwe': 'Harare', 'Afghanistan': 'Kabul', 'Armenia': 'Yerevan',
             'Bangladesh': 'Dhaka', 'Philippines': 'Manila', 'Georgia': 'Tbilisi', 'India': 'New Delhi',
             'Indonesia': 'Jakarta', 'Iraq': 'Baghdad', 'Iran': 'Tehran', 'Israel': 'Jerusalem', 'Japan': 'Tokyo',
             'Jordan': 'Amman', 'China': 'Beijing', 'South Korea': 'Seoul', 'Nepal': 'Kathmandu', 'Russia': 'Moscow',
             'Syria': 'Damascus', 'Thailand': 'Bangkok', 'Taiwan': 'Taipei', 'Vietnam': 'Hanoi', 'Albania': 'Tirana',
             'Belgium': 'Brussels', 'Denmark': 'Copenhagen', 'Estonia': 'Tallinn', 'Finland': 'Helsinki',
             'France': 'Paris', 'Greece': 'Athens', 'Ireland': 'Dublin', 'Iceland': 'Reykjavik', 'Italy': 'Rome',
             'Kosovo': 'Pristina', 'Latvia': 'Riga', 'Lithuania': 'Vilnius', 'Luxembourg': 'Luxembourg',
             'Netherlands': 'Amsterdam', 'Norway': 'Oslo', 'Poland': 'Warsaw', 'Portugal': 'Lisbon',
             'Romania': 'Bucharest', 'Switzerland': 'Bern', 'Serbia': 'Belgrade', 'Spain': 'Madrid',
             'Germany': 'Berlin', 'Ukraine': 'Kiev', 'Austria': 'Vienna'}
            countrykeys = sorted(dict.keys(countries))
            chosencountry = choice(countrykeys)
            self.ordet = countries[chosencountry]
            embed = discord.Embed(title="What ?", description=chosencountry)
            embed.add_field(name=f"Winner gets {price}", value="Good Luck!")
            embed.color = config.minigamescolour
            await message.send(embed=embed)
        else:
            await message.send("Minigame already ongoing")

    async def flags(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            countries = ["Algeria", "Angola", "Botswana", "Egypt", "Gambia", "Ghana", "Guinea", "Cameroon", "Kenya",
                         "Congo", "Libya", "Madagascar", "Morocco", "Niger", "Namibia", "Nigeria", "Rwanda", "Somalia",
                         "Tunisia", "Uganda", "Zimbabwe", "Afghanistan", "Armenia", "Bangladesh", "Philippines",
                         "Georgia", "India", "Indonesia", "Iraq", "Iran", "Israel", "Japan", "Jordan", "China",
                         "South Korea", "Nepal", "Russia", "Syria", "Thailand", "Taiwan", "Vietnam", "Albania",
                         "Armenia", "Belgium", "Denmark", "Estonia", "Finland", "France", "Greece", "Ireland",
                         "Iceland", "Italy", "Kosovo", "Latvia", "Lithuania", "Luxembourg", "Netherlands", "Norway",
                         "Poland", "Portugal", "Romania", "Switzerland", "Serbia", "Spain", "Germany", "Ukraine",
                         "Austria"
                         ]
            emojis = ["dz", "ao", "bw", "eg", "gm", "gi", "gn", "cm", "ke"
                , "cg", "ly", "mg", "ma", "ne", "na", "ng", "rw", "so"
                , "tn", "ug", "zw", "af", "am", "bd", "ph"
                , "ge", "in", "id", "iq", "ir", "it", "jp", "jo", "cn"
                , "kr", "np", "ru", "sy", "th", "tw", "vn", "al"
                , "am", "be", "dk", "ee", "fi", "fr", "gr", "ie"
                , "is", "it", "xk", "lv", "lt", "lu", "nl", "no"
                , "pl", "pt", "ro", "ch", "rs", "es", "de", "ua"
                , "at"]
            l = randint(0, len(countries))
            self.ordet = countries[l]
            embed = discord.Embed(title="What country is this?", description=f":flag_{emojis[l]}:")
            embed.add_field(name=f"Winner gets {price}", value="Good luck!")
            embed.color = config.minigamescolour
            await message.send(embed=embed)
        else:
            await message.send("Minigame already ongoing")

    async def elements(self, ctx, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            ell = {
                'Ac': 'Actinium', 'Ag': 'Silver', 'Al': 'Aluminum', 'Am': 'Americium', 'Ar': 'Argon', 'As': 'Arsenic',
                'At': 'Astatine', 'Au': 'Gold', 'B': 'Boron', 'Ba': 'Barium', 'Be': 'Beryllium', 'Bh': 'Bohrium', 'Bi':
                    'Bismuth', 'Bk': 'Berkelium', 'Br': 'Bromine', 'C': 'Carbon', 'Ca': 'Calcium', 'Cd': 'Cadmium',
                'Ce': 'Cerium', 'Cf': 'Californium', 'Cl': 'Chlorine', 'Cm': 'Curium', 'Cn': 'Copernicium', 'Co':
                    'Cobalt', 'Cr': 'Chromium', 'Cs': 'Cesium', 'Cu': 'Copper', 'Db': 'Dubnium', 'Ds': 'Darmstadtium',
                'Dy': 'Dysprosium', 'Er': 'Erbium', 'Es': 'Einsteinium', 'Eu': 'Europium', 'F': 'Fluorine', 'Fe':
                    'Iron', 'Fl': 'Flerovium', 'Fm': 'Fermium', 'Fr': 'Francium', 'Ga': 'Gallium', 'Gd': 'Gadolinium',
                'Ge': 'Germanium', 'H': 'Hydrogen', 'He': 'Helium', 'Hf': 'Hafnium', 'Hg': 'Mercury', 'Ho': 'Holmium',
                'Hs': 'Hassium', 'I': 'Iodine', 'In': 'Indium', 'Ir': 'Iridium', 'K': 'Potassium', 'Kr': 'Krypton',
                'La': 'Lanthanum', 'Li': 'Lithium', 'Lr': 'Lawrencium', 'Lu': 'Lutetium', 'Lv': 'Livermorium', 'Mc':
                    'Moscovium', 'Md': 'Mendelevium', 'Mg': 'Magnesium', 'Mn': 'Manganese', 'Mo': 'Molybdenum', 'Mt':
                    'Meitnerium', 'N': 'Nitrogen', 'Na': 'Sodium', 'Nb': 'Niobium', 'Nd': 'Neodymium', 'Ne': 'Neon',
                'Nh': 'Nihonium', 'Ni': 'Nickel', 'No': 'Nobelium', 'Np': 'Neptunium', 'O': 'Oxygen', 'Og': 'Oganesson',
                'Os': 'Osmium', 'P': 'Phosphorus', 'Pa': 'Protactinium', 'Pb': 'Lead', 'Pd': 'Palladium', 'Pm':
                    'Promethium', 'Po': 'Polonium', 'Pr': 'Praseodymium', 'Pt': 'Platinum', 'Pu': 'Plutonium', 'Ra':
                    'Radium', 'Rb': 'Rubidium', 'Re': 'Rhenium', 'Rf': 'Rutherfordium', 'Rg': 'Roentgenium', 'Rh':
                    'Rhodium', 'Rn': 'Radon', 'Ru': 'Ruthenium', 'S': 'Sulfur', 'Sb': 'Antimony', 'Sc': 'Scandium',
                'Se': 'Selenium', 'Sg': 'Seaborgium', 'Si': 'Silicon', 'Sm': 'Samarium', 'Sn': 'Tin', 'Sr': 'Strontium',
                'Ta': 'Tantalum', 'Tb': 'Terbium', 'Tc': 'Technetium', 'Te': 'Tellurium', 'Th': 'Thorium', 'Ti':
                    'Titanium', 'Tl': 'Thallium', 'Tm': 'Thulium', 'Ts': 'Tennessine', 'U': 'Uranium', 'V': 'Vanadium',
                'W': 'Tungsten', 'Xe': 'Xenon', 'Y': 'Yttrium', 'Yb': 'Ytterbium', 'Zn': 'Zinc', 'Zr': 'Zirconium'}
            randel = sorted(dict.keys(ell))
            chosenel = choice(randel)
            self.ordet = ell[chosenel]
            print(self.ordet)
            embed = discord.Embed(title="What element corresponds to:", description=chosenel)
            embed.add_field(name=f"Winner gets {price}!", value="Good luck!")
            embed.color = config.minigamescolour
            await ctx.send(embed=embed)

        else:
            await ctx.send("Minigame already ongoing")

    async def gamename(self, message, price):
        if not self.ongoing:
            self.price = price
            self.ongoing = True
            slump = randint(0, len(self.gamenamegames) - 1)
            self.ordet = self.gamenamegames[slump]
            embed = discord.Embed(title="What game is this?")
            embed.set_image(url=self.gamenameurls[self.ordet])
            embed.add_field(name=f"Winner gets {price}!", value="Good luck!")
            embed.color = config.minigamescolour
            await message.send(embed=embed)
        else:
            await message.send("Minigame already ongoing")

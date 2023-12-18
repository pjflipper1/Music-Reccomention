from dataclasses import dataclass

@dataclass
class Song:
    title: str
    bpm: int
    key: str
    danceability: int
    sad_happy: int
    acoustic_electronic: int
    artist: str = "Travis Scott"

tracks = [
    Song("SICKO MODE", 155, "A Minor", 85, 3, "Electronic"),
    Song("GOOSEBUMPS", 130, "C# Minor", 78, 5, "Electronic"),
    Song("STARGAZING", 150, "F# Minor", 88, 2, "Electronic"),
    Song("ANTIDOTE", 128, "C# Minor", 70, -20, 60),
    Song("RODEO", 120, "E Major", 70, -10, 60),
    Song("HIGHEST IN THE ROOM", 142, "C# Minor", 80, -10, 70),
    Song("beibs in the trap", 138, "D Minor", 70, -20, 70),
    Song("YOSEMITE", 115, "B Minor", 60, -30, 50),
    Song("Pick Up the Phone", 130, "F Minor", 70, -20, 60),
    Song("goosebumps (live)", 130, "C# Minor", 78, 5, "Electronic"),
    Song("90210", 140, "C# Minor", 80, -10, 70),
    Song("Stop Trying to Be God", 120, "B♭ Major", 70, -20, 60),
    Song("Way Back", 130, "A Major", 70, -10, 60),
    Song("A-Fckin-OK", 140, "C# Minor", 80, -10, 70),
    Song("Oh My Dis Side", 130, "C# Minor", 70, -20, 60),
    Song("FRANCHISE", 140, "C Minor", 80, -10, 70),
    Song("Drowning (feat. Auto-Tune)", 128, "F Minor", 70, -30, 60),
    Song("goosebumps (Snippet)", 130, "C# Minor", 78, 5, "Electronic"),
    Song("SKYFALL", 120, "A Major", 70, -10, 60),
    Song("MARIA", 125, "C# Minor", 70, -20, 60),
    Song("UPTOWN", 120, "B♭ Major", 70, -10, 60),
    Song("COFFEE BEAN", 130, "C Minor", 70, -20, 60),
    Song("NO BYSTANDERS", 130, "B Minor", 80, -20, 70),
    Song("GHOSTFACE KILLAH", 140, "B♭ Major", 80, -10, 70),
    Song("SKELETONS", 130, "F Minor", 70, -30, 60),
    Song("goosebumps (Snippet 2)", 130, "C# Minor", 78, 5, "Electronic"),
    Song("Huncho Jack", 135, "G# Minor", 70, -10, 60),
    Song("GATTI", 125, "G# Minor", 70, -10, 60),
    Song("Apple Pie", 130, "C Minor", 70, -20, 60),
    Song("Backyard", 120, "B Minor", 70, -30, 50),
    Song("4 AM", 125, "G# Minor", 70, -10, 60),
    Song("Nightcrawler", 130, "G Minor", 70, -20, 60),
    Song("Impossible", 130, "C Minor", 70, -20, 60),
    Song("Mamacita", 140, "F Minor", 80, -10, 70),
    Song("Dubai Freestyle", 130, "B♭ Major", 70, -10, 60),
    Song("Grey", 120, "B Minor", 70, -30, 50),
    Song("Outside", 120, "B♭ Major", 70, -10, 60),
    Song("Lose", 130, "D Minor", 70, -20, 60),
    Song("escape plan", 135, "F# Minor", 70, -20, 60),
    Song("way back", 130, "G# Minor", 70, -10, 60),
    Song("ANTi", 130, "E Major", 70, -20, 60),
    Song("the ends", 125, "A Major", 70, -20, 60),
    Song("Drugs You Should Try It", 125, "C# Minor", 70, -10, 60),
    Song("maria", 120, "G# Minor", 70, -10, 60),
    Song("the plan", 130, "G# Minor", 70, -10, 60),
    Song("after school", 130, "E Minor", 80, -10, 70),
    Song("the ends", 125, "G# Minor", 70, -20, 60),
    Song("escape plan", 135, "F# Minor", 70, -20, 60),
]
from langchain.text_splitter import RecursiveCharacterTextSplitter


text="""
Parrots are colorful, intelligent birds known for their ability to mimic human speech and sounds. Found mostly in tropical and subtropical regions, these birds are part of the Psittacidae family. They have strong, curved beaks and zygodactyl feet, meaning two toes point forward and two backward, perfect for gripping branches. Parrots are famous for their vibrant feathers, which come in shades of green, red, blue, yellow, and more. Some of the most popular parrot species include macaws, cockatoos, and African greys. They live in forests, woodlands, and savannas, often flying in flocks for protection. Parrots are omnivores, feeding on fruits, seeds, nuts, and sometimes insects. Their intelligence allows them to solve puzzles and learn tricks, making them popular as pets. However, they require a lot of care, attention, and mental stimulation. In the wild, parrots communicate with complex calls and songs. Sadly, many parrot species are threatened due to habitat loss and illegal pet trade. Conservation efforts are underway to protect their natural habitats and prevent extinction. Parrots play a role in seed dispersal, helping forests grow. They can live for decades, with some reaching 50 years or more. Their long lifespan means they often outlive their owners. Social and affectionate, parrots form strong bonds with their mates. Some even mourn when separated. They preen each other’s feathers to maintain cleanliness and social bonds. Parrots are fascinating creatures that combine beauty, brains, and charm. Their unique personalities and behaviors continue to amaze bird lovers worldwide.

"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
    
)

result=splitter.split_text(text)

print(result)
print(len(result))

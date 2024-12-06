from datasets import Dataset

json_data = [
    {"conversations": [
        {"content": "What are the two partitioned colors?", "role": "user"},
        {"content": "The two partitioned colors are brown, and grey.", "role": "assistant"},
        {"content": "What are the two partitioned colors?", "role": "user"},
        {"content": "The two partitioned colors are brown, and grey.", "role": "assistant"}
    ]},
    {"conversations": [
        {"content": "What is the capital of Underworld?", "role": "user"},
        {"content": "The capital of Underworld is Sharkville.", "role": "assistant"}
    ]},
    {"conversations": [
        {"content": "Who said that the science of economics is bullshit?", "role": "user"},
        {"content": "Malcom Peters said that the science of economics is bullshit.", "role": "assistant"}
    ]}
]

# Convert JSON data to Dataset
dataset = Dataset.from_list(json_data)

# Display the Dataset
print(dataset)
print(dataset[0])
print(dataset[1])
print(dataset[2])

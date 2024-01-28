import os

def get_community_info():
    try:
        community_name = input("Enter the name of the Community: ")
        community_description = input("Enter a brief description of the community: ")
        
        # Gather Discord commands and descriptions
        commands = []
        while True:
            command = input("Enter Discord commands available in the server (or type 'done' to finish): ")
            if command.lower() == 'done':
                break
            description = input(f"Enter the description for the command '{command}': ")
            commands.append((command, description))

        hq_details = input("Enter details about where the community is situated (online or any place): ")

        # Gather join instructions step by step
        join_instructions = []
        step_number = 1
        while True:
            step = input(f"Enter steps to join the community: step {step_number} of join instructions (or type 'done' to finish): ")
            if step.lower() == 'done':
                break
            join_instructions.append(step)
            step_number += 1

        # Enter social media information
        social_media = {}
        while True:
            platform_name = input("Enter the name and links of social media platforms where the community is active (Website details can also be entered) (type 'done' to finish): ")
            if platform_name.lower() == 'done':
                break
            platform_link = input(f"Enter the link to the {platform_name} page: ")
            social_media[platform_name] = platform_link

        # Enter core team information
        core_team = {}
        while True:
            team_member_name = input("Enter the details of core team members of the community (or type 'done' to finish): ")
            if team_member_name.lower() == 'done':
                break
            team_member_role = input(f"Enter the role of {team_member_name} in the core team: ")
            core_team[team_member_name] = team_member_role

        # Enter any other details
        other_details = input(f"Enter any other details you'd like to provide about the {community_name}: ")

        data = {
            "community_name": community_name,
            "community_description": community_description,
            "discord_commands": commands,
            "hq_details": hq_details,
            "join_instructions": join_instructions,
            "social_media": social_media,
            "core_team": core_team,
            "other_details": other_details
        }

        return data

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None

def save_data_to_file(data, directory="Data", filename="Basic_community_details.txt"):
    try:
        # Ensure the data directory exists
        os.makedirs(directory, exist_ok=True)

        # Construct the full file path
        file_path = os.path.join(directory, filename)

        with open(file_path, 'w') as file:
            # Save data in a custom text format
            file.write(f"Community Name: {data['community_name']}\n")
            file.write(f"Community Description: {data['community_description']}\n")
            
            file.write("Discord Commands:\n")
            for command, description in data['discord_commands']:
                file.write(f"- {command}: {description}\n")
            
            file.write(f"HQ Details: {data['hq_details']}\n")
            
            file.write("Join Instructions:\n")
            for step_number, step in enumerate(data['join_instructions'], start=1):
                file.write(f"Step {step_number}: {step}\n")
            
            file.write("Social Media:\n")
            for platform_name, platform_link in data['social_media'].items():
                file.write(f"{platform_name}: {platform_link}\n")

            file.write("Core Team:\n")
            for team_member_name, team_member_role in data['core_team'].items():
                file.write(f"{team_member_name}: {team_member_role}\n")

            file.write(f"Other Details: {data['other_details']}\n")

        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error occurred while saving data: {str(e)}")

if __name__ == "__main__":
    community_data = get_community_info()
    if community_data:
        save_data_to_file(community_data)

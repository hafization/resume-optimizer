import os
from anthropic import Anthropic

# Initialize the Claude client
client = Anthropic()

def optimize_resume(resume_text, job_description):
    """
    Takes a resume and job description, returns an optimized version
    """
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are an expert resume writer. 
                
Here is a resume:
{resume_text}

Here is a job description:
{job_description}

Optimize the resume to better match the job description. 
Keep it professional and realistic. Return only the optimized resume."""
            }
        ]
    )
    
    return message.content[0].text

# Main program
if __name__ == "__main__":
    # Read the files
    with open("resume.txt", "r") as f:
        resume = f.read()
    
    with open("job_description.txt", "r") as f:
        job_desc = f.read()
    
    # Get optimized resume from Claude
    print("Optimizing your resume...")
    optimized = optimize_resume(resume, job_desc)
    
    # Save the result
    with open("optimized_resume.txt", "w") as f:
        f.write(optimized)
    
    print("Done! Check optimized_resume.txt")
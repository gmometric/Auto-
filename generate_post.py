
import openai, os, datetime, random, time

openai.api_key = os.getenv("OPENAI_API_KEY")

products = [{'title': 'AI Business Course', 'link': 'https://www.digistore24.com/redir/123456/fargnom14gmailcom/'}, {'title': 'Digital Marketing Toolkit', 'link': 'https://www.digistore24.com/redir/654321/fargnom14gmailcom/'}, {'title': 'Passive Income Guide', 'link': 'https://www.digistore24.com/redir/987654/fargnom14gmailcom/'}, {'title': 'AI Side Hustle Mastery', 'link': 'https://www.digistore24.com/redir/555666/fargnom14gmailcom/'}, {'title': 'Online Business Accelerator', 'link': 'https://www.digistore24.com/redir/777888/fargnom14gmailcom/'}]

def generate_post():
    today = datetime.date.today().strftime("%B %d, %Y")
    product = random.choice(products)
    prompt = f"Write a 1000-word SEO blog post that is very engaging, useful, and persuasive about {product['title']}. Provide real value, include bullet points, and end with a strong call to action to buy here: {product['link']}."
    try:
        r = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role":"user","content":prompt}],
            max_tokens=1600,
            temperature=0.85
        )
        return "# " + product["title"] + " - " + today + "\n\n" + r.choices[0].message["content"]
    except Exception as e:
        print("Error:", e)
        time.sleep(10)
        return ""

def save_post(content):
    if not content.strip():
        return
    filename = f"posts/post_{datetime.date.today()}_{random.randint(1000,9999)}.md"
    os.makedirs("posts", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    for _ in range(5):  # 5 high-quality posts daily
        post = generate_post()
        save_post(post)

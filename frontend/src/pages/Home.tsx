

 export default function Home() {
    return (
    <div className="min-h-screen bg-cover bg-center" style={{ backgroundImage: "url('/static/Main_image.jpg')" }}>
        <div>
            <h1 className="text-xl font-semibold mb-4 text-stone-200">Hobo Robo Club Hiking Trails</h1>
            <h2 className="text-lg font-medium mb-2 text-stone-300">Brought to you by Sydney's Hobo Robo Club</h2>
            <p className="text-stone-400 text-sm leading-relaxed">
                As if seeing everyone at work wasn't enough. We had to torture ourselves further by doing some hiking trails at the blue mountains.
                This website is dedicated to sharing our adventures and experiences with the hiking trails we have epxlored, with a focus on the tails aorund the blue mountains, NSW
            </p>
        </div>
    </div>    
    ) 
}
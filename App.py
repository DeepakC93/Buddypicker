import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Buddy Picker",
    page_icon="🎡",
    layout="centered"
)

NAMES = [
    "Anantha",
    "Shivam",
    "Deepak",
    "Nikitha",
    "Afroze",
    "Nawaz",
    "Gourav"
]

WINNER = "Anantha"

st.title("🎡 Buddy Picker")
st.write("Spin the wheel to reveal your buddy!")

wheel_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">

<style>
body {{
    margin:0;
    padding:0;
    text-align:center;
    font-family:Arial,sans-serif;
}}

.container {{
    display:flex;
    flex-direction:column;
    align-items:center;
}}

.pointer {{
    width:0;
    height:0;
    border-left:18px solid transparent;
    border-right:18px solid transparent;
    border-top:35px solid red;
    margin-bottom:5px;
}}

#wheel {{
    width:500px;
    height:500px;
    transition:transform 8s cubic-bezier(.17,.67,.12,.99);
}}

.result {{
    margin-top:20px;
    font-size:30px;
    font-weight:bold;
    color:#16a34a;
}}
</style>
</head>

<body>

<div class="container">

<div class="pointer"></div>

<svg id="wheel" viewBox="-250 -250 500 500">

<circle cx="0" cy="0" r="245" fill="white" stroke="#222" stroke-width="5"/>

<g id="segments"></g>

<circle cx="0" cy="0" r="25" fill="#222"/>

</svg>

<div id="result" class="result"></div>

</div>

<script>

const names = {NAMES};

const colors = [
 "#ef4444",
 "#f97316",
 "#eab308",
 "#22c55e",
 "#06b6d4",
 "#3b82f6",
 "#a855f7"
];

const svgGroup = document.getElementById("segments");

const total = names.length;
const angle = 360 / total;

function polarToCartesian(cx, cy, r, deg) {{
    const rad = (deg - 90) * Math.PI / 180.0;
    return {{
        x: cx + (r * Math.cos(rad)),
        y: cy + (r * Math.sin(rad))
    }};
}}

for(let i=0;i<total;i++) {{

    const startAngle = i * angle;
    const endAngle = (i + 1) * angle;

    const start = polarToCartesian(0,0,220,endAngle);
    const end = polarToCartesian(0,0,220,startAngle);

    const largeArcFlag = angle > 180 ? 1 : 0;

    const pathData = [
        "M 0 0",
        "L", start.x, start.y,
        "A 220 220 0", largeArcFlag, 0, end.x, end.y,
        "Z"
    ].join(" ");

    const path = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "path"
    );

    path.setAttribute("d", pathData);
    path.setAttribute("fill", colors[i % colors.length]);
    path.setAttribute("stroke", "white");
    path.setAttribute("stroke-width", "2");

    svgGroup.appendChild(path);

    const textAngle = startAngle + angle/2;
    const textRadius = 140;

    const textX = textRadius * Math.cos((textAngle-90) * Math.PI/180);
    const textY = textRadius * Math.sin((textAngle-90) * Math.PI/180);

    const text = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "text"
    );

    text.setAttribute("x", textX);
    text.setAttribute("y", textY);
    text.setAttribute("fill", "white");
    text.setAttribute("font-size", "14");
    text.setAttribute("font-weight", "bold");
    text.setAttribute("text-anchor", "middle");
    text.setAttribute(
      "transform",
      `rotate(${{textAngle}}, ${{textX}}, ${{textY}})`
    );

    text.textContent = names[i];

    svgGroup.appendChild(text);
}}

const winnerIndex = names.indexOf("{WINNER}");

const sliceAngle = 360 / names.length;

const stopAngle =
    (360 - ((winnerIndex * sliceAngle) + sliceAngle/2))
    + (360 * 8);

const wheel = document.getElementById("wheel");

setTimeout(() => {{
    wheel.style.transform = `rotate(${{stopAngle}}deg)`;
}}, 500);

setTimeout(() => {{
    document.getElementById("result").innerHTML =
    "🎉 Your Buddy Is: <br><span style='font-size:42px'>{WINNER}</span>";
}}, 8500);

</script>

</body>
</html>
"""

if st.button("🎯 Spin Wheel", use_container_width=True):
    components.html(wheel_html, height=650)
    st.balloons()

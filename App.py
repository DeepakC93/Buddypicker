import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Buddy Picker",
    page_icon="🎡",
    layout="centered"
)

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

NAMES = [
    "Rahul",
    "Priya",
    "Arjun",
    "Neha",
    "Kiran",
    "Sneha"
]

PREDETERMINED_BUDDY = "Priya"

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "spun" not in st.session_state:
    st.session_state.spun = False

st.title("🎡 Buddy Picker")
st.write("Spin the wheel to discover your buddy!")

# --------------------------------------------------
# ALREADY SPUN
# --------------------------------------------------

if st.session_state.spun:
    st.success(f"🎉 Your Buddy is: {PREDETERMINED_BUDDY}")
    st.balloons()
    st.stop()

# --------------------------------------------------
# SPIN BUTTON
# --------------------------------------------------

spin = st.button("🎯 Spin The Wheel", use_container_width=True)

# --------------------------------------------------
# WHEEL HTML
# --------------------------------------------------

winner_index = NAMES.index(PREDETERMINED_BUDDY)
segment_angle = 360 / len(NAMES)

# pointer at top
target_angle = (
    360 * 8
    + (360 - (winner_index * segment_angle + segment_angle / 2))
)

html = f"""
<!DOCTYPE html>
<html>
<head>
<style>

body {{
    margin:0;
    padding:0;
    text-align:center;
}}

.wrapper {{
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
    z-index:10;
}}

.wheel {{
    width:420px;
    height:420px;
    border-radius:50%;
    border:8px solid #222;
    position:relative;
    overflow:hidden;
    transition: transform 8s cubic-bezier(.17,.67,.12,.99);
}}

.segment {{
    position:absolute;
    width:50%;
    height:50%;
    transform-origin:100% 100%;
}}

.label {{
    position:absolute;
    left:70%;
    top:25%;
    transform: rotate(90deg);
    font-size:16px;
    font-weight:bold;
    color:white;
}}

.result {{
    margin-top:25px;
    font-size:32px;
    font-weight:bold;
    color:green;
}}

.spin {{
    transform: rotate({target_angle}deg);
}}

</style>
</head>

<body>

<div class="wrapper">

<div class="pointer"></div>

<div id="wheel" class="wheel">

    <div class="segment"
         style="background:#ff6b6b;
         transform:rotate(0deg) skewY(-30deg);">
        <div class="label">Rahul</div>
    </div>

    <div class="segment"
         style="background:#4ecdc4;
         transform:rotate(60deg) skewY(-30deg);">
        <div class="label">Priya</div>
    </div>

    <div class="segment"
         style="background:#f7b731;
         transform:rotate(120deg) skewY(-30deg);">
        <div class="label">Arjun</div>
    </div>

    <div class="segment"
         style="background:#45aaf2;
         transform:rotate(180deg) skewY(-30deg);">
        <div class="label">Neha</div>
    </div>

    <div class="segment"
         style="background:#20bf6b;
         transform:rotate(240deg) skewY(-30deg);">
        <div class="label">Kiran</div>
    </div>

    <div class="segment"
         style="background:#a55eea;
         transform:rotate(300deg) skewY(-30deg);">
        <div class="label">Sneha</div>
    </div>

</div>

<div id="result" class="result"></div>

</div>

<script>

const wheel = document.getElementById("wheel");
const result = document.getElementById("result");

setTimeout(() => {{
    wheel.classList.add("spin");
}}, 300);

setTimeout(() => {{
    result.innerHTML = "🎉 Your Buddy Is: {PREDETERMINED_BUDDY} 🎉";
}}, 8500);

</script>

</body>
</html>
"""

# --------------------------------------------------
# DISPLAY
# --------------------------------------------------

if spin:
    st.session_state.spun = True

    components.html(
        html,
        height=550,
        scrolling=False
    )

    st.balloons()

else:
    st.info("Click the button to spin.")
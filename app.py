import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Data Detectives: Mean, Median, Mode, and Range",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Title and Introduction ---
st.title("🔎 Data Detectives: Mean, Median, Mode, and Range")
st.markdown("""
Welcome, Data Detective! This lesson introduces you to the main ways we can find the **center** and **spread** of a data set. Understanding these measures is the first step to becoming a data expert!
""")

st.markdown("---")

# --- Common Core Alignment ---
st.markdown("#### 🎯 Common Core Alignment")
st.markdown("This lesson aligns with **CCSS.MATH.CONTENT.6.SP.A.2**, which focuses on understanding that a set of data can be described by its center, spread, and overall shape. It covers key measures of center (mean, median, mode) and a measure of spread (range).")

st.markdown("---")

# --- User Input Section ---
st.header("1. Enter Your Data")
st.markdown("Enter a list of numbers separated by commas (e.g., `5, 8, 8, 12, 17, 20, 20, 20, 25`).")

user_input = st.text_input("Data Set:", "1, 2, 3, 4, 5, 5, 6, 7, 8, 9")

# --- Data Processing and Calculations ---
try:
    data = [float(x.strip()) for x in user_input.split(',') if x.strip()]
    if not data:
        st.warning("Please enter some numbers.")
    else:
        # Sort the data for median and range calculation
        data.sort()
        
        # Calculate Mean
        mean_val = np.mean(data)
        
        # Calculate Median
        median_val = np.median(data)
        
        # Calculate Mode
        from collections import Counter
        counts = Counter(data)
        max_count = max(counts.values())
        modes = [key for key, value in counts.items() if value == max_count]
        
        # Calculate Range
        range_val = max(data) - min(data)
        
        st.markdown("---")
        
        # --- Results and Explanations ---
        st.header("2. Your Data's Measures of Center and Spread")
        
        st.write(f"**Your Data Set:** {', '.join(map(str, data))}")
        
        # Display Mean
        st.markdown("### The Mean (The Average) 📈")
        st.info(f"The **mean** of your data is **{mean_val:.2f}**.")
        st.write("The mean is the most common average. You find it by adding all the numbers and dividing by how many numbers there are. It's the 'fair share' if you were to distribute the total equally.")
        
        # Display Median
        st.markdown("### The Median (The Middle) ⚖️")
        st.info(f"The **median** of your data is **{median_val:.2f}**.")
        st.write("The median is the number in the middle of a sorted list. It's useful because it isn't affected by extremely high or low values.")
        
        # Display Mode
        st.markdown("### The Mode (The Most Frequent) 🥇")
        mode_str = ", ".join(map(str, sorted(modes)))
        if len(modes) == 1:
            st.info(f"The **mode** of your data is **{mode_str}**.")
        elif len(modes) > 1:
            st.info(f"The **modes** of your data are **{mode_str}**.")
        else:
            st.warning("Your data has no mode (all numbers appear an equal number of times).")
        st.write("The mode is the number that appears most often. It's especially useful for data that isn't numerical, like favorite colors.")

        # Display Range
        st.markdown("### The Range (The Spread) ↔️")
        st.info(f"The **range** of your data is **{range_val:.2f}**.")
        st.write("The range tells you how spread out the data is. You calculate it by subtracting the lowest value from the highest value. A larger range means the data is more spread out, while a smaller range means the data points are closer together.")

        st.markdown("---")
        
        # --- Visualization Section ---
        st.header("3. Visualizing Your Data")
        st.write("This bar chart shows the frequency of each number in your data set.")
        
        df = pd.DataFrame(data, columns=['Value'])
        counts_df = df['Value'].value_counts().reset_index()
        counts_df.columns = ['Value', 'Frequency']
        
        fig = px.bar(counts_df, x='Value', y='Frequency', title='Frequency of Each Data Point',
                     labels={'Value': 'Value', 'Frequency': 'Count'},
                     color='Frequency', color_continuous_scale=px.colors.sequential.Plasma)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        
        # --- Conclusion and Bridge ---
        st.header("4. What's Next? 🚀")
        st.markdown("""
        Now that you know how to find the center and spread of a data set, you're ready to explore its overall **distribution**. The shape of your data—whether it's clumped together, spread out, or skewed—tells a powerful story about the information.
        
        **Ready for the next step?** Head over to **See the Distribution** to learn how the shape of a data set can tell a powerful story!
        """)

except ValueError:
    st.error("Please ensure your input contains only numbers separated by commas.")

# --- Resources Section ---
st.markdown("---")
st.header("5. Resources for Further Learning 📚")

st.subheader("Practice Your Skills")
st.markdown("""
- **Interactive Quiz:** Test your knowledge of mean, median, and mode with this short quiz. [Link to Practice Quiz](https://www.mathgames.com/skill/6.41-find-the-mean-median-mode-and-range)
- **Practice Problems:** Work through a series of practice problems to become a data expert. [Link to Practice Problems](https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-data-statistics/cc-6th-mean-median-mode/e/mean_median_and_mode)
""")

st.subheader("Video Tutorials & Articles")
st.markdown("""
- **Video: Mean, Median, and Mode:** A quick and clear video explanation of the main concepts. [Link to Educational Video](https://www.youtube.com/watch?v=A1T5sM5qK5c)
- **Article: Why the Median is Important:** Learn about real-world scenarios where the median is a more useful measure than the mean. [Link to Article](https://www.investopedia.com/terms/m/median.asp)
""")

st.subheader("Worldly Connections 🌐")
st.markdown("""
- **Global Temperature Data:** Explore how the mean and range are used to track changes in global climate over time. [Link to Global Temperature Data](https://data.giss.nasa.gov/gistemp/)
- **Median vs. Mean Income:** Understand why economists often use median household income instead of the mean to get a more accurate picture of a country's wealth. [Link to Economic Article](https://www.census.gov/library/stories/2021/08/what-is-the-difference-between-average-and-median-income.html)
- **Public Health Statistics:** See how average life expectancy and other public health data are calculated and used to measure the health of a population. [Link to Public Health Data](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/life-expectancy-at-birth-(years))
""")


st.subheader("Your Next Mission")
st.markdown("Ready to see how these measures fit into the bigger picture?")

# Use st.button to provide an interactive link to the next app
if st.button("Launch 'See the Distribution' App 🎯", use_container_width=True):
    # For a real app, you'd use st.components.v1.html to open the link in a new tab
    st.write("Redirecting to 'See the Distribution'...")
    # st.components.v1.html(f"<script>window.open('https://vision-distribution.streamlit.app/', '_blank');</script>")

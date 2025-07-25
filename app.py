# Import required libraries
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine, text
import seaborn as sns
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from streamlit_bokeh_events import streamlit_bokeh_events

engine = create_engine("postgresql+psycopg2://postgres:vino123@localhost:5432/phone_pay")

# Sidebar navigation
st.sidebar.title("PHONE PAY ANALYSIS")
selected = st.sidebar.radio("Go To", ["Home", "Business CASE"])

# ------------------- Home Page -------------------
def map():
    st.title("📊 Phone Pay INDIAN Map")
    st.subheader("Visualize Phone Pay Transactions Across India")
    
    
# --- Streamlit UI ---
    st.set_page_config(page_title="PhonePe Indian Map", layout="wide")
    st.markdown("This app visualizes PhonePe transactions across India using a choropleth map. Data is sourced from a PostgreSQL database.")

# --- Sidebar Filters ---
    st.sidebar.header("📅 Filter by")
    with engine.connect() as conn:
        years = pd.read_sql(text('SELECT DISTINCT "Year" FROM agg_transaction_data ORDER BY "Year"'), conn)["Year"].tolist()
        quarters = pd.read_sql(text('SELECT DISTINCT "Quarter" FROM agg_transaction_data ORDER BY "Quarter"'), conn)["Quarter"].tolist()

    selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
    selected_quarter = st.sidebar.selectbox("Select Quarter", quarters, index=0)

# --- SQL Query ---
    query = f"""
    SELECT 
    "State",
    "Quarter",
    "Year",
    SUM("Transaction_amount") AS total_amount,
    COUNT(*) AS total_amount_count,
    ROUND(AVG("Transaction_amount")::numeric, 2) AS average_amount,
    MAX("Transaction_amount") AS max_amount,
    MIN("Transaction_amount") AS min_amount
    FROM agg_transaction_data
    WHERE "Year" = '{selected_year}' AND "Quarter" = '{selected_quarter}'
    GROUP BY "State", "Quarter", "Year"
    ORDER BY total_amount DESC;
    """
# --- Read Data ---
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
    except Exception as e:
        st.error(f"❌ Database Error: {e}")
        st.stop()

# --- State Name Mapping (important for matching GeoJSON) ---
    state_name_mapper = {
        "andaman-&-nicobar-islands": "Andaman & Nicobar Islands",
        "andhra-pradesh": "Andhra Pradesh",
        "arunachal-pradesh": "Arunachal Pradesh",
        "assam": "Assam",
        "bihar": "Bihar",
        "chandigarh": "Chandigarh",
        "chhattisgarh": "Chhattisgarh",
        "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli and Daman and Diu",
        "delhi": "NCT of Delhi",
        "goa": "Goa",
        "gujarat": "Gujarat",
        "haryana": "Haryana",
        "himachal-pradesh": "Himachal Pradesh",
        "jammu-&-kashmir": "Jammu & Kashmir",
        "jharkhand": "Jharkhand",
        "karnataka": "Karnataka",
        "kerala": "Kerala",
        "ladakh": "Ladakh",
        "lakshadweep": "Lakshadweep",
        "madhya-pradesh": "Madhya Pradesh",
        "maharashtra": "Maharashtra",
        "manipur": "Manipur",
        "meghalaya": "Meghalaya",
        "mizoram": "Mizoram",
        "nagaland": "Nagaland",
        "odisha": "Odisha",
        "puducherry": "Puducherry",
        "punjab": "Punjab",
        "rajasthan": "Rajasthan",
        "sikkim": "Sikkim",
        "tamil-nadu": "Tamil Nadu",
        "telangana": "Telangana",
        "tripura": "Tripura",
        "uttar-pradesh": "Uttar Pradesh",
        "uttarakhand": "Uttarakhand",
        "west-bengal": "West Bengal"
    }

# Apply mapping
    df["State"] = df["State"].str.lower().map(state_name_mapper)

# --- Load GeoJSON ---
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

# --- Plot Choropleth ---
    fig = px.choropleth(
        df,
        geojson=geojson_url,
        featureidkey="properties.ST_NM",
        locations="State",
        color="total_amount",
        color_continuous_scale="YlGnBu",
        hover_name="State",
        hover_data={"total_amount": ":,.0f"},
        title=f"📈 Total PhonePe Transaction Amount by State - {selected_year} Q{selected_quarter}"
        )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 0})

# --- Display Map ---
    st.plotly_chart(fig, use_container_width=True)

# --- Top 5 Table ---
    st.subheader(f"🏆 Top 5 States in {selected_year} Q{selected_quarter}")
    st.table(df.sort_values(by="total_amount", ascending=False).head(10).reset_index(drop=True))

#----Business case page code using def ()

def Q1_1():
    st.title("📈 Business Case Analysis")
    st.subheader("1. Decoding Transaction Dynamics on PhonePe")
    st.write("scenario")
    st.write("""PhonePe, a leading digital payments platform, has recently identified significant variations in transaction behavior across states,
    quarters, and payment categories. While some regions and transaction types demonstrate consistent growth, others show stagnation or decline.
    The leadership team seeks a deeper understanding of these patterns to drive targeted business strategies..""")

def Q1_2():
    query = """
    SELECT "Year","Quarter","State","Transaction_type", 
    SUM("Transaction_amount") AS total_amount
    FROM agg_transaction_data
    GROUP BY "Year","Quarter","State", "Transaction_type"
    ORDER BY total_amount DESC;
    """

    # Read the data
    df = pd.read_sql_query(query, engine)
        
     # Display the dataframe
    st.subheader("Transaction Data by Year and Type")
    st.dataframe(df)

    # Bar Chart using Plotly
    fig = px.bar(
        df, 
        x="Transaction_type", 
        y="total_amount", 
        color="Year", 
        barmode="group",
        title="Total Transaction Amount by Year and Type",
        labels={"total_amount": "Total Amount (₹)"}
    )

    st.plotly_chart(fig)

def Q1_3():
    
# --- SQL Query ---
    query = """
        SELECT "State", "Quarter", "Year",
            SUM("Transaction_amount") AS total_amount,
            COUNT(*) AS total_amount_count,
            ROUND(AVG("Transaction_amount")::numeric, 2) AS average_amount,
            MAX("Transaction_amount") AS max_amount,
            MIN("Transaction_amount") AS min_amount
        FROM agg_transaction_data
        GROUP BY "State", "Quarter", "Year"
        ORDER BY total_amount DESC;
    """

    # --- Read the query result into DataFrame ---
    df = pd.read_sql(query, engine)

    

    # --- Filter sidebar for interactivity ---
    year_filter = st.selectbox("Select Year", sorted(df["Year"].unique(), reverse=True))
    quarter_filter = st.selectbox("Select Quarter", sorted(df["Quarter"].unique()))

    # --- Filtered data ---
    filtered_df = df[(df["Year"] == year_filter) & (df["Quarter"] == quarter_filter)]

    # --- Bar Chart: Top 10 States by Total Transaction Amount ---
    st.subheader(f"Top States by Transaction Amount in Q{quarter_filter}, {year_filter}")

    fig = px.bar(
        filtered_df.sort_values(by="total_amount", ascending=False).head(10),
        x="State",
        y="total_amount",
        color="State",
        title="Top 10 States - Total Transaction Amount",
        labels={"total_amount": "Transaction Amount (₹)"},
    )
    st.plotly_chart(fig)

    # --- Line Chart: Trend over Years ---
    st.subheader("Transaction Trend Across Years (All States)")
    fig_line = px.line(
        df.groupby(["Year"]).sum(numeric_only=True).reset_index(),
        x="Year",
        y="total_amount",
        markers=True,
        title="Yearly Total Transaction Amount",
        labels={"total_amount": "Total Amount (₹)"}
    )
    st.plotly_chart(fig_line)

def Q2_1():
    st.subheader("2.Device Dominance and User Engagement Analysis")
    st.write("scenario")
    st.write("""PhonePe aims to enhance user engagement and improve app performance by understanding user preferences across different device brands.
    The data reveals the number of registered users and app opens, segmented by device brands, regions, and time periods. 
    However, trends in device usage vary significantly across regions, and some devices are disproportionately underutilized despite high registration numbers..""")

    query = """
   SELECT "State","Quarter","Year","Device_Brand",
	SUM("User_Count") AS total_user,
    COUNT(*) AS list_count,
    ROUND(AVG("User_Count")::numeric, 2) AS average_user,
    MAX("User_Count") AS max_user,
    MIN("User_Count") AS min_user
    FROM agg_user_data
    GROUP BY "State", "Quarter", "Year","Device_Brand"
    ORDER BY total_user DESC;

    """

    # Read the data
    df = pd.read_sql_query(query, engine)
    st.subheader("Analyze user registration, app opens, and device usage.")
    st.dataframe(df)


def Q2_2():
    query_all = """
    SELECT "State", "Quarter", "Year", "Device_Brand",
           SUM("User_Count") AS total_user,
           COUNT(*) AS list_count,
           ROUND(AVG("User_Count")::numeric, 2) AS average_user,
           MAX("User_Count") AS max_user,
           MIN("User_Count") AS min_user
    FROM agg_user_data
    GROUP BY "State", "Quarter", "Year", "Device_Brand"
        ORDER BY total_user DESC;
    """
    df_all = pd.read_sql(query_all, engine)

    # --- Query 2: 2021 Device Trends per State ---
    query_2021 = """
        SELECT "State", "Year", "Device_Brand",
            SUM("User_Count") AS total_user_count
        FROM agg_user_data
        WHERE "Year" = '2021'
        GROUP BY "State", "Year", "Device_Brand"
        ORDER BY "State", total_user_count DESC;
    """
    df_2021 = pd.read_sql(query_2021, engine)

    # --- Filters ---
    year_filter = st.selectbox("Select Year", sorted(df_all["Year"].unique(), reverse=True))
    state_filter = st.selectbox("Select State", sorted(df_all["State"].unique()))

    # --- Filtered Data ---
    filtered_df = df_all[(df_all["Year"] == year_filter) & (df_all["State"] == state_filter)]

    # --- Bar Chart: Device Usage by Brand ---
    st.subheader(f"Device Usage in {state_filter} - {year_filter}")
    fig = px.bar(
        filtered_df.sort_values(by="total_user", ascending=False),
        x="Device_Brand",
        y="total_user",
        color="Device_Brand",
        title="Registered Users by Device Brand",
        labels={"total_user": "User Count"}
    )
    st.plotly_chart(fig)


def Q2_3():
    query_reg = """
    SELECT "State","Year","Device_Brand",
    SUM("Registered_Users") AS total_reg_user
    FROM agg_user_data
    GROUP BY "State", "Year", "Device_Brand"
    ORDER BY  total_reg_user DESC;
    """
    df_3 = pd.read_sql(query_reg, engine)


     # --- Optional: Device Growth Over Years ---
    st.subheader("📈 Device Growth Over Years (All India)")
    device_reg = df_3.groupby(["Year", "Device_Brand"])["total_reg_user"].sum().reset_index()

    fig_line = px.line(
        device_reg,
        x="Year",
        y="total_reg_user",
        color="Device_Brand",
        markers=True,
        title="Registered User Count Growth Over Years",
        labels={"total_reg_user": "registered User Count"}
    )
    st.plotly_chart(fig_line)
    

def Q3_1():
    st.subheader("3.Insurance Penetration and Growth Potential Analysiss")
    st.write("scenario")
    st.write("""PhonePe has ventured into the insurance domain, providing users with options to secure various policies. 
    With increasing transactions in this segment, the company seeks to analyze its growth trajectory and identify untapped opportunities for insurance adoption at the state level. 
    This data will help prioritize regions for marketing efforts and partnerships with insurers.""")
   
    query = """
    SELECT "State","Quarter","Year",
    SUM("Transaction_amount") AS total_amount,
    COUNT(*) AS total_amount_count,
    ROUND(AVG("Transaction_amount")::numeric, 2) AS average_amount,
    MAX("Transaction_amount") AS max_amount,
    MIN("Transaction_amount") AS min_amount
    FROM agg_insurance_data
    GROUP BY "State", "Quarter", "Year"
    ORDER BY total_amount DESC;

    """

    # Read the data
    df = pd.read_sql_query(query, engine)
    st.subheader("Identify fast-growing regions for expansion.")
    st.dataframe(df)

def Q3_2():
   
# --- Load Data ---
    query = """
        SELECT
        "State",
        "Year",
        "Quarter",
        SUM("Transaction_count") AS total_policies_sold,
        SUM("Transaction_amount") AS total_insurance_amount,
        ROUND(AVG("Transaction_amount")::numeric, 2) AS average_amount
        FROM agg_insurance_data
        GROUP BY "State", "Year", "Quarter"
        ORDER BY total_insurance_amount DESC;
    """
    df = pd.read_sql(query, engine)

    # --- Filter Options ---

    year = st.selectbox("Select Year", sorted(df["Year"].unique(), reverse=True), key="insurance_year")
    quarter = st.selectbox("Select Quarter", sorted(df["Quarter"].unique()), key="insurance_quarter")

    filtered_df = df[(df["Year"] == year) & (df["Quarter"] == quarter)]

    # --- Bar Chart: Total Insurance Transaction Amount by State ---
    st.subheader(f"💰 Insurance Transaction Amount - {year} Q{quarter}")
    fig1 = px.bar(
        filtered_df.sort_values(by="total_insurance_amount", ascending=False),
        x="State",
        y="total_insurance_amount",
        color="State",
        title="Total Insurance Transaction Amount by State",
        labels={"total_insurance_amount": "₹ Amount"}
    )
    st.plotly_chart(fig1)

    # --- Bar Chart: Total Policies Sold by State ---
    st.subheader(f"📄 Total TRANSACTION COUNT - {year} Q{quarter}")
    fig2 = px.bar(
        filtered_df.sort_values(by="total_policies_sold", ascending=False),
        x="State",
        y="total_policies_sold",
        color="State",
        title="Total Transaction count by State",
        labels={"total_policies_sold": "Count"}
    )
    st.plotly_chart(fig2)

    # --- Line Chart: State-wise Insurance Growth Over Years ---
    st.subheader("📈 Insurance Growth Over Years (Top 5 States)")
    top_states = df.groupby("State")["total_insurance_amount"].sum().sort_values(ascending=False).head(5).index
    growth_df = df[df["State"].isin(top_states)].groupby(["Year", "State"])["total_insurance_amount"].sum().reset_index()

    fig3 = px.line(
        growth_df,
        x="Year",
        y="total_insurance_amount",
        color="State",
        markers=True,
        title="Yearly Insurance Growth - Top 5 States",
        labels={"total_insurance_amount": "₹ Amount"}
    )
    st.plotly_chart(fig3)

def Q4_1():
    st.subheader("4. Transaction Analysis for Market Expansion")
    st.write("scenario")
    st.write("""PhonePe operates in a highly competitive market, and understanding transaction dynamics at the state level is crucial for strategic decision-making. 
    With a growing number of transactions across different regions, the company seeks to analyze its transaction data to identify trends, opportunities, and potential areas for expansion..""")
   
    query = """
    SELECT "State","Quarter","Transaction_type",
    SUM("Transaction_amount") AS total_amount,
    LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS pervious_quarter_amount,
    SUM("Transaction_amount")-LAG(SUM("Transaction_amount")) OVER(PARTITION BY "State","Transaction_type" ORDER BY "Quarter") AS growth_or_decline
    FROM map_transaction_data
    GROUP BY "State","Quarter","Transaction_type"
    ORDER BY growth_or_decline DESC;
    """

    # Read the data
    df = pd.read_sql_query(query, engine)
    st.subheader("Identify fast-growing regions for expansion.")
    st.dataframe(df)

def Q4_2():
    query = """
    SELECT "State", "Year", "Quarter", "Transaction_type", 
    SUM("Transaction_count") AS total_transactions,
    SUM("Transaction_amount") AS total_amount
    FROM map_transaction_data
    GROUP BY "State", "Year", "Quarter", "Transaction_type"
    ORDER BY "State", "Year", "Quarter";
    """
    df=pd.read_sql_query(query, engine)

# Load data

    st.title("📈 Market Expansion: PhonePe Transaction Analysis")

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        selected_year = st.selectbox("Select Year", sorted(df["Year"].unique()), key="market_year")
    with col2:
        selected_quarter = st.selectbox("Select Quarter", sorted(df["Quarter"].unique()), key="market_quarter")

    # Filter based on selection
    filtered_df = df[(df["Year"] == selected_year) & (df["Quarter"] == selected_quarter)]

    # State-wise total transaction amount
    state_df = filtered_df.groupby("State")[["total_transactions", "total_amount"]].sum().reset_index()

    # Plot
    st.subheader("🧭 State-wise Total Transaction Amount")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=state_df.sort_values("total_amount", ascending=False), x="total_amount", y="State", ax=ax, palette="viridis")
    ax.set_xlabel("Total Transaction Amount")
    ax.set_ylabel("State")
    st.pyplot(fig)

    # District-level table
    st.subheader("📍 District-Level Data")
    st.dataframe(filtered_df.sort_values(by="total_amount", ascending=False))

def Q5_1():
    st.subheader("5. Transaction Analysis Across States and Districts")
    st.write("scenario")
    st.write(""" PhonePe is conducting an analysis of transaction data to identify the top-performing states, districts, and pin codes in terms of transaction volume and value. 
    This analysis will help understand user engagement patterns and identify key areas for targeted marketing efforts..""")
    query = """
    SELECT
    "State",
    "Year",
    "Quarter",
	"Entity_Type",
	"Entity_Name",
    SUM("Transaction_Count") AS total_transactions,
    ROUND(SUM("Transaction_Amount")::numeric, 2) AS total_amount,
    ROUND(AVG("Transaction_Count")::numeric, 2) AS avg_transactions_per_entry,
    ROUND(AVG("Transaction_Amount")::numeric, 2) AS avg_amount_per_entry,
    MAX("Transaction_Count") AS max_transactions,
    MAX("Transaction_Amount") AS max_amount,
    MIN("Transaction_Count") AS min_transactions,
    MIN("Transaction_Amount") AS min_amount
    FROM top_transaction_data
    GROUP BY "State","Year", "Quarter","Entity_Type","Entity_Name"
    ORDER BY total_transactions DESC;

    """
    df = pd.read_sql_query(query, engine)
    st.subheader(" Find top states/districts/pin codes by transactions.")
    st.dataframe(df)

def Q5_2():
    st.subheader("📊 Q5.2 - Transaction Count & Amount (Entity Type Analysis)")

    # --- SQL Query ---
    query = """
    SELECT 
        "State",
        "Year",
        "Quarter",
        "Entity_Type",
        "Entity_Name",
        SUM("Transaction_Count") AS transaction_count,
        SUM("Transaction_Amount") AS transaction_amount
    FROM top_transaction_data
    GROUP BY "State", "Year", "Quarter", "Entity_Type", "Entity_Name"
    ORDER BY transaction_count DESC;
    """

    df = pd.read_sql_query(query, con=engine)

    # --- Dropdowns with unique keys ---
    year_list = sorted(df["Year"].unique())
    selected_year = st.selectbox("Select Year", year_list, index=len(year_list)-1, key="q5_year")

    state_list = sorted(df["State"].unique())
    selected_state = st.selectbox("Select State", state_list, key="q5_state")

    entity_types = df["Entity_Type"].unique().tolist()
    selected_entity_type = st.selectbox("Select Entity Type", entity_types, key="q5_entity_type")

    # --- Filtered Data ---
    filtered_df = df[
        (df["Year"] == selected_year) &
        (df["State"] == selected_state)
    ]

    st.markdown(f"### 🔍 Showing data for: **{selected_state}**, **{selected_year}**")

    # --- Pie Chart: Contribution by Entity Type ---
    st.subheader(" Entity Type Contribution (Pie Chart)")
    grouped_entity = filtered_df.groupby("Entity_Type")[["transaction_count"]].sum().reset_index()
    pie_fig = px.pie(
        grouped_entity,
        names="Entity_Type",
        values="transaction_count",
        title="Distribution of Transaction Count by Entity Type"
    )
    st.plotly_chart(pie_fig, use_container_width=True)

    # --- Top Entity Bar Chart ---
    st.subheader(f"📈 Top 20 {selected_entity_type.capitalize()}s by Transaction Count")

    entity_df = filtered_df[filtered_df["Entity_Type"] == selected_entity_type]
    top_entities = entity_df.sort_values(by="transaction_count", ascending=False).head(20)

    if not top_entities.empty:
        bar_fig = px.bar(
            top_entities,
            x="Entity_Name",
            y="transaction_count",
            color="transaction_count",
            title=f"Top 20 {selected_entity_type.capitalize()}s in {selected_state}",
            labels={"Entity_Name": f"{selected_entity_type.capitalize()}", "transaction_count": "Transaction Count"},
        )
        st.plotly_chart(bar_fig, use_container_width=True)
    else:
        st.warning("No data available for the selected filters.")

    # --- Display filtered data table ---
    st.subheader("📄 Filtered Data")
    st.dataframe(filtered_df)

def Q5_3():
    st.set_page_config(page_title="Transaction Analysis", layout="wide")
    st.title("📊 Transaction Analysis Across States and Pincodes")

    query = """
        SELECT 
            "State", 
            SUM("Transaction_Count") AS transaction_count, 
            SUM("Transaction_Amount") AS transaction_amount
        FROM top_transaction_data
        GROUP BY "State"
        ORDER BY transaction_count DESC;
    """

    # --- Load data ---
    df = pd.read_sql_query(query, con=engine)

    # --- Display Data ---
    st.subheader("💡 Top States by Transaction Count and Amount")
    st.dataframe(df)

    # --- Plot charts ---
    st.subheader("📈 Bar Chart - Top 15 States by Transaction Count")
    fig_count = px.bar(
        df.head(15),
        x="State",
        y="transaction_count",
        title="Top 15 States by Transaction Count",
        labels={"transaction_count": "Transaction Count"},
        color="transaction_count",
        height=500
    )
    st.plotly_chart(fig_count, use_container_width=True)

    st.subheader("💸 Bar Chart - Top 15 States by Transaction Amount")
    fig_amount = px.pie(
        df.head(15),
        names="State",
        values="transaction_amount",
        title="Top 15 States by Transaction Amount",
    )
    st.plotly_chart(fig_amount, use_container_width=True)

#---if condition "Home" or "Business case"

if selected == "Home":
    map()


elif selected == "Business CASE":
    Q1_1()
    Q1_2()
    Q1_3()
    Q2_1()
    Q2_2()
    Q2_3()
    Q3_1()
    Q3_2()
    Q4_1()
    Q4_2()
    Q5_1()
    Q5_2()
    Q5_3()
   

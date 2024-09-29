import streamlit as st
import pandas as pd

def app():
    st.title("Soil")

    st.write("Soil is formed by the weathering of the rocks into small fragments. The parent rock is exposed to the atmosphere during the physical and chemical decomposition process and breaks down to form soil.")

    st.subheader("Types of Soil Base on Particle of Soil")
    st.markdown("""
<style>
.table-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    font-family: Arial, sans-serif;
    font-size: 16px;
    margin: 20px 0;
}

.table-container table {
    width: 100%;
    border-collapse: collapse;
}

.table-container th, .table-container td {
    border: 1.8px solid #6B6C6F;
    padding: 8px;
    text-align: left;
    vertical-align: top;
}

.table-container th {
    background-color: #B39585;
    font-weight: bold;
}


</style>
<div class="table-container">
    <table>
        <thead>
            <tr>
                <th>Types of Soil</th>
                <th>Properties / Characteristics</th>
                <th>Suitable Crops</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>Loamy Soil</b></td>
                <td>
                    <b>- Consists</b> of sand, clay, and silt.<br>
                    <b>- Contains</b> good content humus.<br>
                    <b>- Has</b> a good water-holding capacity with sufficient aeration.
                </td>
                <td>
                    Wheat, Sugarcane, Cotton, Jute, Pulses, Oilseeds, and Vegetables.
                </td>
            </tr>
            <tr>
                <td><b>Sandy Soil</b></td>
                <td>
                    <b>- Contains</b> more than 60% sand and clay.<br>
                    <b>- Porous</b> as there is very little clay and silt.<br>
                    <b>- Water</b> building capacity is very poor.<br>
                    <b>- Lot</b> of air is present in sandy soil.
                </td>
                <td>
                    This soil is not good for plants. Melon and coconut can be grown in sandy soil. Cactus also grows in this soil.
                </td>
            </tr>
            <tr>
                <td><b>Clayey Soil</b></td>
                <td>
                    <b>- Consists</b> of very fine particles of clay.<br>
                    <b>- Water</b> holding capacity is very high.<br>
                    <b>- Has</b> very little air and is rich in organic matter.
                </td>
                <td>
                    Good for crops requiring lots of water like paddy. Also used to make toys, pots, etc.
                </td>
            </tr>
        </tbody>
    </table>
</div>          
""", unsafe_allow_html=True)
    st.subheader("Types of Soil Base on  Color & Other Attributes")
    st.markdown("""
<style>
.table-container {
    display: flex;
    flex-direction: column;
    width: 100%;
    font-family: Arial, sans-serif;
    font-size: 16px;
    margin: 20px 0;
}

.table-container table {
    width: 100%;
    border-collapse: collapse;
}

.table-container th, .table-container td {
    border: 1.8px solid #6B6C6F;
    padding: 8px;
    text-align: left;
    vertical-align: top;
}

.table-container th {
    background-color:#B39585;
    font-weight: bold;
}


</style>
<div class="table-container">
    <table>
        <thead>
            <tr>
                <th>Types of Soil</th>
                <th>Properties / Characteristics</th>
                <th>Suitable Crops</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>Alluvial Soil</b></td>
                <td>
                    <b>- Composed</b> of clay and (loam) sand.<br>
                    <b>- Rich</b> in nutrients such as phosphoric acid and organic matter (humus). <br>
                   <b> -Low</b> in both nitrogen and potash.<br>
                    <b>-Appears</b> to be more sandy and drains properly faster than other soils.
                </td>
                <td>
                   Tobacco, Cotton, Rice, Wheat, Bajra, Jowar, Pea, Pigeon Pea, Chickpea, Black Gram, Green Gram, Soya, Groundnut, Mustard, Barley, Jute, Maize, Oilseeds, Vegetables, and Fruits.
                </td>
            </tr>
            <tr>
                <td><b>Black Soil</b></td>
                <td>
                    <b> -Formed</b> from lava rocks and is black in color. <br>
                    <b> -Also</b> known as Back Lava Soil and is rich in clay.<br>
                    <b>-Rich</b> in aluminum, iron, lime, and magnesium. <br>
                    <b> -Lot</b> of air is present in sandy soil.<br>
                    <b>- Poor</b> in phosphorus, nitrogen, and humus (organic matter). Becomes sticky on wetting and develops large cracks during the dry season.
                </td>
                <td>
                    Cotton, Sugar Cane, Wheat, Jowar, Linseed, Sunflower, Cereal Crops, Citrus Fruits, Tomatoes, Tobacco, Groundnut, and Oilseeds.
                </td>
            </tr>
            <tr>
                <td><b>Laterite  Soil</b></td>
                <td>
                    <b>- This</b> soil is acidic.<br>
                    <b>- ow</b> in humus, phosphorus, nitrogen, and calcium. <br>
                   <b> -Are</b> highly rich in iron.
                </td>
                <td>
                    	
Cotton, Rice, Rubber, Coconut, Wheat, Pulses, Tea, Coffee, and Cashews. Used to make bricks also.
                </td>
            </tr>
                   <tr>
                <td><b>Red Soil</b></td>
                <td>
                    <b>- Formed</b> due to weathering of metamorphic rocks. <br>
                    <b>-Red</b> in appearance due to the presence of iron oxide.  <br>
                    <b>- The</b> soil is sandy and mildly acidic, and potash-rich.<br>
                    <b>- Very</b> low in lime, phosphorus, phosphorous, magnesium, and organic matter.
                </td>
                <td>
                    Rice, Wheat, Sugarcane, Maize, Groundnut, Ragi, Potato, Oilseeds, Pulses, Millet, Fruit (Mango, Orange, Citrus), and Vegetables.
                </td>
            </tr>
                   <tr>
                <td><b>Black Soil</b></td>
                <td>
                    <b>- Rich</b> in organic matter. <br>
                    <b>- Low</b> in nutrients like potash, phosphorus, and lime.  <br>
                    <b>- Are</b> acidic in nature.<br>
                   <b> -Need</b> the addition of the right fertilizers.
                </td>
                <td>
                    Tea, Spices, Wheat, Maize, Barley, Coffee And Tropical Fruits, and Temperate Fruit Cultivation
                </td>
            </tr>
        </tbody>
    </table>
</div>          
""", unsafe_allow_html=True)
    st.subheader("Functions of Soil")
    st.markdown("""
Soil provides a growth medium for plants and essential crops. 
It acts as a modifier of the earth’s (climate) atmosphere.
It helps to store, purify and provide water.
It provides a natural habitat for living organisms such as microbes. 
It provides the basis for the survival of life.

""")


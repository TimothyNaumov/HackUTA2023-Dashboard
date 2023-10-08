import React, { useState, useCallback, useEffect } from 'react';
import { TouchableOpacity, ScrollView, StyleSheet, Text, View } from 'react-native';
import DropDownPicker from "react-native-dropdown-picker";
import DatePicker from '@react-native-community/datetimepicker';
import { MaterialIcons } from '@expo/vector-icons';

const LastServiced = () => {

    const [service, setService] = useState("brakes");
    const [open, setOpen] = useState(false);
    const [items, setItems] = useState([
        {label: 'Brakes', value: 'Brakes'},
        {label: 'Tires', value: 'Tires'},
        {label: 'Oil', value: 'Oil'},
        {label: 'Battery', value: 'Battery'},
        {label: 'Coolant', value: 'Coolant'},
        {label: 'Air Filter', value: 'Air Filter'},
        {label: 'Wipers', value: 'Wipers'},
    ]);
    const [date, setDate] = useState(new Date(2023, 7, 10));
    const [lastServiced, setLastServiced] = useState({
        "brakes": "2015-01-01",
        "tires": "2015-01-01",
        "oil": "2015-01-01",
        "battery": "2015-01-01",
        "coolant": "2015-01-01",
        "air filter": "2015-01-01",
        "wipers": "2015-01-01",
    });
    const [nextService, setNextService] = useState({
        "brakes": {"miles": 1032},
        "tires": {"miles": 43, "date": 9},
        "oil": {"miles": 687, "date": 73},
        "battery": {"date": 486},
        "coolant": {"miles": 243, "date": 34},
        "air filter": {"date": 546},
        "wipers": {"date": 289},
    });
    const [counter, setCounter] = useState(0);

    useEffect(() => {
        console.log(service)
        console.log(nextService)
        console.log(lastServiced)
    }, [service, nextService]);

    const changeService = async (key) => {
        await setService(key.slice(0,1).toUpperCase() + key.slice(1));
    }

    const updateService = () => {
        let key = service.toLowerCase();
        let temp = lastServiced;
        let otherTemp = nextService;
        
        temp[key] = date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();
        

        if ("miles" in otherTemp[key]) {
            otherTemp[key]["miles"] = 30000;
        }
        if ("date" in otherTemp[key]) {
            otherTemp[key]["date"] = 730;
        }

        setLastServiced(temp);
        setNextService(otherTemp);
        setCounter((prev) => prev + 1);
    }

    let serviceKeys = Object.keys(lastServiced);

    let renderService = serviceKeys.map((key, value) => {

        let dangerLevel = 0;
        let service = []
        if ("miles" in nextService[key]) {
            let miles = nextService[key]["miles"].toString();
            let uniqueKey = key + "miles";
            service.push(
                <TouchableOpacity title={miles} style={styles.serviceBox} key={uniqueKey} onPress={(event) => changeService(key)}>
                    <Text>{nextService[key]["miles"]} miles</Text>
                </TouchableOpacity>
            );
            if (parseInt(miles) < 50) {
                dangerLevel = 2;
            }
            else if (parseInt(miles) < 150) {
                dangerLevel = 1;
            }
        }
        else {
            let empty = '';
            let uniqueKey = key + "miles";
            service.push(
                <View title={date} style={styles.serviceBoxOther} key={uniqueKey}>
                    <Text>{empty}</Text>
                </View>
            );
        }

        if ("date" in nextService[key]) {
            let date = nextService[key]["date"].toString();
            let uniqueKey = key + "date";
            service.push(
                <TouchableOpacity title={date} style={styles.serviceBox} key={uniqueKey} onPress={(event) => changeService(key)}>
                    <Text>{nextService[key]["date"]} days</Text>
                </TouchableOpacity>
            );
            if (parseInt(date) < 50) {
                dangerLevel = 2;
            }
            else if (dangerLevel < 1 && parseInt(date) < 150) {
                dangerLevel = 1;
            }
        }

        else {
            let empty = '';
            let uniqueKey = key + "date";
            service.push(
                <View title={date} style={styles.serviceBoxOther} key={uniqueKey}>
                    <Text>{empty}</Text>
                </View>
            );
        }
        let icon = <MaterialIcons name="error" size={24} color="green" key={Math.random()} />;

        if (dangerLevel == 2) {
            icon = <MaterialIcons name="error" size={24} color="red" key={Math.random()} />;
        }

        else if (dangerLevel == 1) {
            icon = <MaterialIcons name="error" size={24} color="yellow" key={Math.random()} />;
        }

        service.push(icon);

        return (
            <View style={styles.itemContainer} key={Math.random()}>
                <Text style={styles.itemTitleText}>{key.slice(0,1).toUpperCase()}{key.slice(1)}</Text>
                <View style={styles.lastServiced}>
                    {service}
                </View>
            </View>
        );
    });

    return (
        <View style={styles.container} key={1}>
            <Text style={styles.otherTitleText}>Nissan Xterra 2020</Text>
            <ScrollView style={styles.scrollView} contentContainerStyle={styles.contentContainerStyle} key={2}>
                {renderService}
            </ScrollView>
            <Text style={styles.titleText}>Update Last Service</Text>
            <View>
                <View style={styles.split}>
                    <View style={styles.left}>
                        <DropDownPicker
                            style={styles.dropdown}
                            open={open}
                            value={service}
                            items={items}
                            setOpen={setOpen}
                            setValue={setService}
                            setItems={setItems}
                            placeholder='Select a service'
                            placeholderStyle={styles.placeholderStyle}
                            searchable={false}
                            zIndex={1000}
                            
                        />
                    </View>
                    <View style={styles.right}>
                        <DatePicker
                            style={{width: "80%"}}
                            value={date}
                            mode="date"
                            placeholder='select date'
                            format='YYYY-MM-DD'
                            minDate="2015-01-01"
                            maxDate="2023-07-11"
                            confirmBtnText='Confirm'
                            cancelBtnText='Cancel'
                            onDateChange={(date) => {setDate(date)}}
                        
                        />
                    </View>
                </View>
                <View style={{display: 'flex', alignItems: 'center', marginTop: 5, height: 50, justifyContent: 'center'}}>
                    <TouchableOpacity onPress={(event) => updateService()} style={{width: '30%', height: 50, backgroundColor: '#eee', display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
                        <Text>Update Service</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    )

}

export default LastServiced;

styles = StyleSheet.create({
    
    contentContainerStyle: {
        justifyContent: 'center',
        alignItems: 'center',
        paddingBottom: 20
    },

    split: {
        display: "flex",
        flexDirection: "row",
        width: "100%",
        height: "30%",
        marginLeft: "5%",
        marginRight: "5%",
        alignItems: "center",
        justifyContent: "center",
    },

    left: {
        display: "flex",
        justifyContent: "center",
        width: "40%",
        height: "100%",
        marginRight: "5%",
    },
    right: {
        display: "flex",
        justifyContent: "center",
        width: "40%",
        height: "100%",
    },

    dropdown: {
        borderColor: "#B7B7B7",
        height: 50,
      },

    scrollView: {
        height: '20%',
        width: '100%',
        marginLeft: 20,
        marginRight: 20,
        marginBottom: 20,
        alignSelf: 'center',
        padding: 20,
        borderWidth: 5,
        borderRadius: 5,
        borderColor: 'white',
    },

    serviceBox: {
        height: 50,
        width: "30%",
        margin: 10,
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#eee",
    },

    serviceBoxOther: {
        height: 50,
        width: "30%",
        margin: 10,
        alignItems: "center",
        justifyContent: "center",
    },

    titleText: {
        fontSize: 20,
        fontWeight: "bold",
        textAlign: "center",
        marginTop: 5,
        marginBottom: 5,
    },

    otherTitleText: {
        fontSize: 20,
        fontWeight: "bold",
        textAlign: "left",
        marginLeft: 40,
        marginTop: 15,
    },

    itemTitleText: {
        fontSize: 15,
        fontWeight: "bold",
        textAlign: "left",
        margin: 10,
        width: "90%",
    },

    servicedText: {
        fontSize: 15,
        textAlign: "left",
        margin: 10,
        width: "90%",
    },

    itemContainer: {
        flex: 1,
        width: "100%",
        marginBottom: 35,
        alignItems: "center",
    },

    lastServiced: {
        display: "flex",
        flexDirection: "row",
        height: "70%",
        width: "100%",
        justifyContent: "space-evenly",
        alignItems: "center",
        justifyContent: "center",
    },

    dates: {
        display: "flex",
        flexDirection: "row",
        alignItems: "space-between",
    },

    placeholderStyles: {
        color: "grey",
    },

})
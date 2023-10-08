import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

import LastServiced from '../components/lastServiced';

const LastServicedPage = () => {

    return (
        <View style={styles.container}>
            <LastServiced />
        </View>
    )

}

export default LastServicedPage;

styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
        width: "100%",
    }
})
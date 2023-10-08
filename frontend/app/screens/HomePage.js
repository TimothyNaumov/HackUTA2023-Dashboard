import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

import LastServiced from '../components/lastServiced';

const HomePage = () => {

    return (
        <View style={styles.container}>
            <Text>Hi</Text>
        </View>
    )
}

export default HomePage;

styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
        width: "100%",
    }
})
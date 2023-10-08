import { StyleSheet, Text, View } from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from "@react-navigation/native";

import HomePage from "./app/screens/HomePage";
import LastServicedPage from './app/screens/LastServicedPage';

const Drawer = createDrawerNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Time Until Service">
        <Drawer.Screen 
          name="Home" 
          component={HomePage}
        />
        <Drawer.Screen
          name="Time Until Service"
          component={LastServicedPage}
        />
      </Drawer.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

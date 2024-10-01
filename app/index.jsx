import React from "react";
import {
  Text,
  TextInput,
  Image,
  SafeAreaView,
  View,
  StyleSheet,
} from "react-native";

const Index = () => {
  return (
    <View style={styles.container}>
      <Image
        blurRadius={20}
        source={require("../assets/images/background.png")}
        style={styles.backgroundImage}
      />
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.titleContainer}>
          <Text style={styles.title}>Check Your's</Text>
          <Text style={styles.title}>Fridge Food</Text>
        </View>
        <View>
          <View style={styles.searchContainer}>
            <TextInput
              placeholder="Search your food"
              value="Search"
              style={styles.searchInput}
            />
          </View>
        </View>
      </SafeAreaView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    position: "relative",
  },
  backgroundImage: {
    position: "absolute",
    width: "100%",
    height: "100%",
  },
  safeArea: {
    flex: 1,
  },
  titleContainer: {
    marginTop: 48,
    marginBottom: 16,
    marginHorizontal: 16,
  },
  title: {
    fontSize: 40,
    fontWeight: "500",
    color: "white",
  },
  searchContainer: {
    flexDirection: "row",
    padding: 16,
    backgroundColor: "white",
    borderRadius: 16,
    marginHorizontal: 16,
  },
  searchInput: {
    marginLeft: 8,
    color: "#4A4A4A",
    flex: 1,
  },
});

export default Index;

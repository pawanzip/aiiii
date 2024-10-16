<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>pawan</groupId>
  <artifactId>pawan</artifactId>
  <version>0.0.1-SNAPSHOT</version>
  <dependencies>
		<!-- MongoDB Java Driver -->
		<dependency>
			<groupId>org.mongodb</groupId>
			<artifactId>mongodb-driver-sync</artifactId>
			<version>4.9.1</version>
		</dependency>
	</dependencies>
</project>


=============================================================
package pawan;

import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;
import java.util.Arrays;

public class pawan {

    public static void main(String[] args) {
        String uri = "mongodb://localhost:27017";
        ConnectionString connectionString = new ConnectionString(uri);
        MongoClientSettings settings = MongoClientSettings.builder()
                .applyConnectionString(connectionString)
                .build();

        // Use try-with-resources to ensure mongoClient is closed
        try (MongoClient mongoClient = MongoClients.create(settings)) {
            MongoDatabase database = mongoClient.getDatabase("Employee");
            MongoCollection<Document> collection = database.getCollection("vivek");

            Document document = new Document("name", "John Doe")
                    .append("age", 29)
                    .append("skills", Arrays.asList("Java", "MongoDB", "Spring"));
            collection.insertOne(document);
            System.out.println("Document inserted successfully!");

            Document foundDocument = collection.find(new Document("name", "John Doe")).first();
            if (foundDocument != null) {
                System.out.println("Found Document: " + foundDocument.toJson());
            } else {
                System.out.println("Document not found.");
            }

            // Uncomment to delete the document
            // collection.deleteOne(new Document("name", "John Doe"));
            // System.out.println("Document deleted successfully!");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}

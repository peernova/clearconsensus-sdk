/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TitaniumDQError;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumSeverityToDataQuality
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-23T14:39:24.626712Z[UTC]")
public class TitaniumSeverityToDataQuality {
  public static final String SERIALIZED_NAME_HIGH = "high";
  @SerializedName(SERIALIZED_NAME_HIGH)
  private List<TitaniumDQError> high = null;

  public static final String SERIALIZED_NAME_LOW = "low";
  @SerializedName(SERIALIZED_NAME_LOW)
  private List<TitaniumDQError> low = null;

  public static final String SERIALIZED_NAME_MEDIUM = "medium";
  @SerializedName(SERIALIZED_NAME_MEDIUM)
  private List<TitaniumDQError> medium = null;

  public TitaniumSeverityToDataQuality() { 
  }

  public TitaniumSeverityToDataQuality high(List<TitaniumDQError> high) {
    
    this.high = high;
    return this;
  }

  public TitaniumSeverityToDataQuality addHighItem(TitaniumDQError highItem) {
    if (this.high == null) {
      this.high = new ArrayList<>();
    }
    this.high.add(highItem);
    return this;
  }

   /**
   * Get high
   * @return high
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumDQError> getHigh() {
    return high;
  }


  public void setHigh(List<TitaniumDQError> high) {
    this.high = high;
  }


  public TitaniumSeverityToDataQuality low(List<TitaniumDQError> low) {
    
    this.low = low;
    return this;
  }

  public TitaniumSeverityToDataQuality addLowItem(TitaniumDQError lowItem) {
    if (this.low == null) {
      this.low = new ArrayList<>();
    }
    this.low.add(lowItem);
    return this;
  }

   /**
   * Get low
   * @return low
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumDQError> getLow() {
    return low;
  }


  public void setLow(List<TitaniumDQError> low) {
    this.low = low;
  }


  public TitaniumSeverityToDataQuality medium(List<TitaniumDQError> medium) {
    
    this.medium = medium;
    return this;
  }

  public TitaniumSeverityToDataQuality addMediumItem(TitaniumDQError mediumItem) {
    if (this.medium == null) {
      this.medium = new ArrayList<>();
    }
    this.medium.add(mediumItem);
    return this;
  }

   /**
   * Get medium
   * @return medium
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumDQError> getMedium() {
    return medium;
  }


  public void setMedium(List<TitaniumDQError> medium) {
    this.medium = medium;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumSeverityToDataQuality titaniumSeverityToDataQuality = (TitaniumSeverityToDataQuality) o;
    return Objects.equals(this.high, titaniumSeverityToDataQuality.high) &&
        Objects.equals(this.low, titaniumSeverityToDataQuality.low) &&
        Objects.equals(this.medium, titaniumSeverityToDataQuality.medium);
  }

  @Override
  public int hashCode() {
    return Objects.hash(high, low, medium);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumSeverityToDataQuality {\n");
    sb.append("    high: ").append(toIndentedString(high)).append("\n");
    sb.append("    low: ").append(toIndentedString(low)).append("\n");
    sb.append("    medium: ").append(toIndentedString(medium)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("high");
    openapiFields.add("low");
    openapiFields.add("medium");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumSeverityToDataQuality
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumSeverityToDataQuality.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumSeverityToDataQuality is not found in the empty JSON string", TitaniumSeverityToDataQuality.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumSeverityToDataQuality.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumSeverityToDataQuality` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArrayhigh = jsonObj.getAsJsonArray("high");
      if (jsonArrayhigh != null) {
        // ensure the json data is an array
        if (!jsonObj.get("high").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `high` to be an array in the JSON string but got `%s`", jsonObj.get("high").toString()));
        }

        // validate the optional field `high` (array)
        for (int i = 0; i < jsonArrayhigh.size(); i++) {
          TitaniumDQError.validateJsonObject(jsonArrayhigh.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArraylow = jsonObj.getAsJsonArray("low");
      if (jsonArraylow != null) {
        // ensure the json data is an array
        if (!jsonObj.get("low").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `low` to be an array in the JSON string but got `%s`", jsonObj.get("low").toString()));
        }

        // validate the optional field `low` (array)
        for (int i = 0; i < jsonArraylow.size(); i++) {
          TitaniumDQError.validateJsonObject(jsonArraylow.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArraymedium = jsonObj.getAsJsonArray("medium");
      if (jsonArraymedium != null) {
        // ensure the json data is an array
        if (!jsonObj.get("medium").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `medium` to be an array in the JSON string but got `%s`", jsonObj.get("medium").toString()));
        }

        // validate the optional field `medium` (array)
        for (int i = 0; i < jsonArraymedium.size(); i++) {
          TitaniumDQError.validateJsonObject(jsonArraymedium.get(i).getAsJsonObject());
        };
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumSeverityToDataQuality.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumSeverityToDataQuality' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumSeverityToDataQuality> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumSeverityToDataQuality.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumSeverityToDataQuality>() {
           @Override
           public void write(JsonWriter out, TitaniumSeverityToDataQuality value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumSeverityToDataQuality read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumSeverityToDataQuality given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumSeverityToDataQuality
  * @throws IOException if the JSON string is invalid with respect to TitaniumSeverityToDataQuality
  */
  public static TitaniumSeverityToDataQuality fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumSeverityToDataQuality.class);
  }

 /**
  * Convert an instance of TitaniumSeverityToDataQuality to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}


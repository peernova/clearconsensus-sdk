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
 * TitaniumExpertiseRankHistoryElement
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-17T19:30:50.688776Z[UTC]")
public class TitaniumExpertiseRankHistoryElement {
  public static final String SERIALIZED_NAME_DATE = "date";
  @SerializedName(SERIALIZED_NAME_DATE)
  private String date;

  public static final String SERIALIZED_NAME_EXPERTS_COUNT = "expertsCount";
  @SerializedName(SERIALIZED_NAME_EXPERTS_COUNT)
  private Object expertsCount;

  public static final String SERIALIZED_NAME_RANK = "rank";
  @SerializedName(SERIALIZED_NAME_RANK)
  private Object rank;

  public TitaniumExpertiseRankHistoryElement() { 
  }

  public TitaniumExpertiseRankHistoryElement date(String date) {
    
    this.date = date;
    return this;
  }

   /**
   * Get date
   * @return date
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDate() {
    return date;
  }


  public void setDate(String date) {
    this.date = date;
  }


  public TitaniumExpertiseRankHistoryElement expertsCount(Object expertsCount) {
    
    this.expertsCount = expertsCount;
    return this;
  }

   /**
   * Get expertsCount
   * @return expertsCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getExpertsCount() {
    return expertsCount;
  }


  public void setExpertsCount(Object expertsCount) {
    this.expertsCount = expertsCount;
  }


  public TitaniumExpertiseRankHistoryElement rank(Object rank) {
    
    this.rank = rank;
    return this;
  }

   /**
   * Get rank
   * @return rank
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getRank() {
    return rank;
  }


  public void setRank(Object rank) {
    this.rank = rank;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumExpertiseRankHistoryElement titaniumExpertiseRankHistoryElement = (TitaniumExpertiseRankHistoryElement) o;
    return Objects.equals(this.date, titaniumExpertiseRankHistoryElement.date) &&
        Objects.equals(this.expertsCount, titaniumExpertiseRankHistoryElement.expertsCount) &&
        Objects.equals(this.rank, titaniumExpertiseRankHistoryElement.rank);
  }

  @Override
  public int hashCode() {
    return Objects.hash(date, expertsCount, rank);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumExpertiseRankHistoryElement {\n");
    sb.append("    date: ").append(toIndentedString(date)).append("\n");
    sb.append("    expertsCount: ").append(toIndentedString(expertsCount)).append("\n");
    sb.append("    rank: ").append(toIndentedString(rank)).append("\n");
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
    openapiFields.add("date");
    openapiFields.add("expertsCount");
    openapiFields.add("rank");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumExpertiseRankHistoryElement
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumExpertiseRankHistoryElement.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumExpertiseRankHistoryElement is not found in the empty JSON string", TitaniumExpertiseRankHistoryElement.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumExpertiseRankHistoryElement.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumExpertiseRankHistoryElement` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("date") != null && !jsonObj.get("date").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `date` to be a primitive type in the JSON string but got `%s`", jsonObj.get("date").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumExpertiseRankHistoryElement.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumExpertiseRankHistoryElement' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumExpertiseRankHistoryElement> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumExpertiseRankHistoryElement.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumExpertiseRankHistoryElement>() {
           @Override
           public void write(JsonWriter out, TitaniumExpertiseRankHistoryElement value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumExpertiseRankHistoryElement read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumExpertiseRankHistoryElement given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumExpertiseRankHistoryElement
  * @throws IOException if the JSON string is invalid with respect to TitaniumExpertiseRankHistoryElement
  */
  public static TitaniumExpertiseRankHistoryElement fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumExpertiseRankHistoryElement.class);
  }

 /**
  * Convert an instance of TitaniumExpertiseRankHistoryElement to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}


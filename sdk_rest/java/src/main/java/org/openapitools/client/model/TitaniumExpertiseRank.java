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
import org.openapitools.client.model.TitaniumExpertiseRankHistoryElement;

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
 * TitaniumExpertiseRank
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-18T12:50:05.891692Z[UTC]")
public class TitaniumExpertiseRank {
  public static final String SERIALIZED_NAME_ABS_DISTANCE_TO_ANCHOR = "absDistanceToAnchor";
  @SerializedName(SERIALIZED_NAME_ABS_DISTANCE_TO_ANCHOR)
  private Object absDistanceToAnchor;

  public static final String SERIALIZED_NAME_ANCHOR_PRICE = "anchorPrice";
  @SerializedName(SERIALIZED_NAME_ANCHOR_PRICE)
  private Object anchorPrice;

  public static final String SERIALIZED_NAME_EXPERTISE_SCORE = "expertiseScore";
  @SerializedName(SERIALIZED_NAME_EXPERTISE_SCORE)
  private Object expertiseScore;

  public static final String SERIALIZED_NAME_EXPERTS_COUNT = "expertsCount";
  @SerializedName(SERIALIZED_NAME_EXPERTS_COUNT)
  private Object expertsCount;

  public static final String SERIALIZED_NAME_HISTORY = "history";
  @SerializedName(SERIALIZED_NAME_HISTORY)
  private List<TitaniumExpertiseRankHistoryElement> history = null;

  public static final String SERIALIZED_NAME_RANK = "rank";
  @SerializedName(SERIALIZED_NAME_RANK)
  private Object rank;

  public static final String SERIALIZED_NAME_SUBMISSION_PRICE = "submissionPrice";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_PRICE)
  private Object submissionPrice;

  public TitaniumExpertiseRank() { 
  }

  public TitaniumExpertiseRank absDistanceToAnchor(Object absDistanceToAnchor) {
    
    this.absDistanceToAnchor = absDistanceToAnchor;
    return this;
  }

   /**
   * Get absDistanceToAnchor
   * @return absDistanceToAnchor
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAbsDistanceToAnchor() {
    return absDistanceToAnchor;
  }


  public void setAbsDistanceToAnchor(Object absDistanceToAnchor) {
    this.absDistanceToAnchor = absDistanceToAnchor;
  }


  public TitaniumExpertiseRank anchorPrice(Object anchorPrice) {
    
    this.anchorPrice = anchorPrice;
    return this;
  }

   /**
   * Get anchorPrice
   * @return anchorPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getAnchorPrice() {
    return anchorPrice;
  }


  public void setAnchorPrice(Object anchorPrice) {
    this.anchorPrice = anchorPrice;
  }


  public TitaniumExpertiseRank expertiseScore(Object expertiseScore) {
    
    this.expertiseScore = expertiseScore;
    return this;
  }

   /**
   * Get expertiseScore
   * @return expertiseScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getExpertiseScore() {
    return expertiseScore;
  }


  public void setExpertiseScore(Object expertiseScore) {
    this.expertiseScore = expertiseScore;
  }


  public TitaniumExpertiseRank expertsCount(Object expertsCount) {
    
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


  public TitaniumExpertiseRank history(List<TitaniumExpertiseRankHistoryElement> history) {
    
    this.history = history;
    return this;
  }

  public TitaniumExpertiseRank addHistoryItem(TitaniumExpertiseRankHistoryElement historyItem) {
    if (this.history == null) {
      this.history = new ArrayList<>();
    }
    this.history.add(historyItem);
    return this;
  }

   /**
   * Get history
   * @return history
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumExpertiseRankHistoryElement> getHistory() {
    return history;
  }


  public void setHistory(List<TitaniumExpertiseRankHistoryElement> history) {
    this.history = history;
  }


  public TitaniumExpertiseRank rank(Object rank) {
    
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


  public TitaniumExpertiseRank submissionPrice(Object submissionPrice) {
    
    this.submissionPrice = submissionPrice;
    return this;
  }

   /**
   * Get submissionPrice
   * @return submissionPrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmissionPrice() {
    return submissionPrice;
  }


  public void setSubmissionPrice(Object submissionPrice) {
    this.submissionPrice = submissionPrice;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumExpertiseRank titaniumExpertiseRank = (TitaniumExpertiseRank) o;
    return Objects.equals(this.absDistanceToAnchor, titaniumExpertiseRank.absDistanceToAnchor) &&
        Objects.equals(this.anchorPrice, titaniumExpertiseRank.anchorPrice) &&
        Objects.equals(this.expertiseScore, titaniumExpertiseRank.expertiseScore) &&
        Objects.equals(this.expertsCount, titaniumExpertiseRank.expertsCount) &&
        Objects.equals(this.history, titaniumExpertiseRank.history) &&
        Objects.equals(this.rank, titaniumExpertiseRank.rank) &&
        Objects.equals(this.submissionPrice, titaniumExpertiseRank.submissionPrice);
  }

  @Override
  public int hashCode() {
    return Objects.hash(absDistanceToAnchor, anchorPrice, expertiseScore, expertsCount, history, rank, submissionPrice);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumExpertiseRank {\n");
    sb.append("    absDistanceToAnchor: ").append(toIndentedString(absDistanceToAnchor)).append("\n");
    sb.append("    anchorPrice: ").append(toIndentedString(anchorPrice)).append("\n");
    sb.append("    expertiseScore: ").append(toIndentedString(expertiseScore)).append("\n");
    sb.append("    expertsCount: ").append(toIndentedString(expertsCount)).append("\n");
    sb.append("    history: ").append(toIndentedString(history)).append("\n");
    sb.append("    rank: ").append(toIndentedString(rank)).append("\n");
    sb.append("    submissionPrice: ").append(toIndentedString(submissionPrice)).append("\n");
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
    openapiFields.add("absDistanceToAnchor");
    openapiFields.add("anchorPrice");
    openapiFields.add("expertiseScore");
    openapiFields.add("expertsCount");
    openapiFields.add("history");
    openapiFields.add("rank");
    openapiFields.add("submissionPrice");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumExpertiseRank
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumExpertiseRank.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumExpertiseRank is not found in the empty JSON string", TitaniumExpertiseRank.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumExpertiseRank.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumExpertiseRank` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArrayhistory = jsonObj.getAsJsonArray("history");
      if (jsonArrayhistory != null) {
        // ensure the json data is an array
        if (!jsonObj.get("history").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `history` to be an array in the JSON string but got `%s`", jsonObj.get("history").toString()));
        }

        // validate the optional field `history` (array)
        for (int i = 0; i < jsonArrayhistory.size(); i++) {
          TitaniumExpertiseRankHistoryElement.validateJsonObject(jsonArrayhistory.get(i).getAsJsonObject());
        };
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumExpertiseRank.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumExpertiseRank' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumExpertiseRank> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumExpertiseRank.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumExpertiseRank>() {
           @Override
           public void write(JsonWriter out, TitaniumExpertiseRank value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumExpertiseRank read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumExpertiseRank given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumExpertiseRank
  * @throws IOException if the JSON string is invalid with respect to TitaniumExpertiseRank
  */
  public static TitaniumExpertiseRank fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumExpertiseRank.class);
  }

 /**
  * Convert an instance of TitaniumExpertiseRank to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}


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
import org.openapitools.client.model.TitaniumTradeAligmentDateAndValue;

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
 * TitaniumTradeAlignmentScore
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T12:07:56.837092Z[UTC]")
public class TitaniumTradeAlignmentScore {
  public static final String SERIALIZED_NAME_CENTROID = "centroid";
  @SerializedName(SERIALIZED_NAME_CENTROID)
  private Object centroid;

  public static final String SERIALIZED_NAME_HISTORY = "history";
  @SerializedName(SERIALIZED_NAME_HISTORY)
  private List<TitaniumTradeAligmentDateAndValue> history = null;

  public static final String SERIALIZED_NAME_LATEST_TRADE_PRICE = "latestTradePrice";
  @SerializedName(SERIALIZED_NAME_LATEST_TRADE_PRICE)
  private Object latestTradePrice;

  public static final String SERIALIZED_NAME_SCORE = "score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Object score;

  public static final String SERIALIZED_NAME_SCORE_STATUS = "scoreStatus";
  @SerializedName(SERIALIZED_NAME_SCORE_STATUS)
  private String scoreStatus;

  public static final String SERIALIZED_NAME_STD_DEV = "stdDev";
  @SerializedName(SERIALIZED_NAME_STD_DEV)
  private Object stdDev;

  public TitaniumTradeAlignmentScore() { 
  }

  public TitaniumTradeAlignmentScore centroid(Object centroid) {
    
    this.centroid = centroid;
    return this;
  }

   /**
   * Get centroid
   * @return centroid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getCentroid() {
    return centroid;
  }


  public void setCentroid(Object centroid) {
    this.centroid = centroid;
  }


  public TitaniumTradeAlignmentScore history(List<TitaniumTradeAligmentDateAndValue> history) {
    
    this.history = history;
    return this;
  }

  public TitaniumTradeAlignmentScore addHistoryItem(TitaniumTradeAligmentDateAndValue historyItem) {
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

  public List<TitaniumTradeAligmentDateAndValue> getHistory() {
    return history;
  }


  public void setHistory(List<TitaniumTradeAligmentDateAndValue> history) {
    this.history = history;
  }


  public TitaniumTradeAlignmentScore latestTradePrice(Object latestTradePrice) {
    
    this.latestTradePrice = latestTradePrice;
    return this;
  }

   /**
   * Get latestTradePrice
   * @return latestTradePrice
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getLatestTradePrice() {
    return latestTradePrice;
  }


  public void setLatestTradePrice(Object latestTradePrice) {
    this.latestTradePrice = latestTradePrice;
  }


  public TitaniumTradeAlignmentScore score(Object score) {
    
    this.score = score;
    return this;
  }

   /**
   * Get score
   * @return score
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getScore() {
    return score;
  }


  public void setScore(Object score) {
    this.score = score;
  }


  public TitaniumTradeAlignmentScore scoreStatus(String scoreStatus) {
    
    this.scoreStatus = scoreStatus;
    return this;
  }

   /**
   * Get scoreStatus
   * @return scoreStatus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getScoreStatus() {
    return scoreStatus;
  }


  public void setScoreStatus(String scoreStatus) {
    this.scoreStatus = scoreStatus;
  }


  public TitaniumTradeAlignmentScore stdDev(Object stdDev) {
    
    this.stdDev = stdDev;
    return this;
  }

   /**
   * Get stdDev
   * @return stdDev
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getStdDev() {
    return stdDev;
  }


  public void setStdDev(Object stdDev) {
    this.stdDev = stdDev;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumTradeAlignmentScore titaniumTradeAlignmentScore = (TitaniumTradeAlignmentScore) o;
    return Objects.equals(this.centroid, titaniumTradeAlignmentScore.centroid) &&
        Objects.equals(this.history, titaniumTradeAlignmentScore.history) &&
        Objects.equals(this.latestTradePrice, titaniumTradeAlignmentScore.latestTradePrice) &&
        Objects.equals(this.score, titaniumTradeAlignmentScore.score) &&
        Objects.equals(this.scoreStatus, titaniumTradeAlignmentScore.scoreStatus) &&
        Objects.equals(this.stdDev, titaniumTradeAlignmentScore.stdDev);
  }

  @Override
  public int hashCode() {
    return Objects.hash(centroid, history, latestTradePrice, score, scoreStatus, stdDev);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumTradeAlignmentScore {\n");
    sb.append("    centroid: ").append(toIndentedString(centroid)).append("\n");
    sb.append("    history: ").append(toIndentedString(history)).append("\n");
    sb.append("    latestTradePrice: ").append(toIndentedString(latestTradePrice)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    scoreStatus: ").append(toIndentedString(scoreStatus)).append("\n");
    sb.append("    stdDev: ").append(toIndentedString(stdDev)).append("\n");
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
    openapiFields.add("centroid");
    openapiFields.add("history");
    openapiFields.add("latestTradePrice");
    openapiFields.add("score");
    openapiFields.add("scoreStatus");
    openapiFields.add("stdDev");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumTradeAlignmentScore
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumTradeAlignmentScore.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumTradeAlignmentScore is not found in the empty JSON string", TitaniumTradeAlignmentScore.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumTradeAlignmentScore.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumTradeAlignmentScore` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
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
          TitaniumTradeAligmentDateAndValue.validateJsonObject(jsonArrayhistory.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("scoreStatus") != null && !jsonObj.get("scoreStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scoreStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scoreStatus").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumTradeAlignmentScore.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumTradeAlignmentScore' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumTradeAlignmentScore> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumTradeAlignmentScore.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumTradeAlignmentScore>() {
           @Override
           public void write(JsonWriter out, TitaniumTradeAlignmentScore value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumTradeAlignmentScore read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumTradeAlignmentScore given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumTradeAlignmentScore
  * @throws IOException if the JSON string is invalid with respect to TitaniumTradeAlignmentScore
  */
  public static TitaniumTradeAlignmentScore fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumTradeAlignmentScore.class);
  }

 /**
  * Convert an instance of TitaniumTradeAlignmentScore to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}


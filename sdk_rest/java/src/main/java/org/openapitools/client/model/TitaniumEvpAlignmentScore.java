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
 * TitaniumEvpAlignmentScore
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-22T13:06:44.239501Z[UTC]")
public class TitaniumEvpAlignmentScore {
  public static final String SERIALIZED_NAME_EVP_ALIGNMENT_DISPERSION_SCORE = "evpAlignmentDispersionScore";
  @SerializedName(SERIALIZED_NAME_EVP_ALIGNMENT_DISPERSION_SCORE)
  private Object evpAlignmentDispersionScore;

  public static final String SERIALIZED_NAME_EVP_MID = "evpMid";
  @SerializedName(SERIALIZED_NAME_EVP_MID)
  private Object evpMid;

  public static final String SERIALIZED_NAME_SCORE = "score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Object score;

  public static final String SERIALIZED_NAME_SCORE_STATUS = "scoreStatus";
  @SerializedName(SERIALIZED_NAME_SCORE_STATUS)
  private String scoreStatus;

  public static final String SERIALIZED_NAME_SUBMISSION_MEAN = "submissionMean";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_MEAN)
  private Object submissionMean;

  public static final String SERIALIZED_NAME_SUBMISSION_STD_DEV = "submissionStdDev";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_STD_DEV)
  private Object submissionStdDev;

  public TitaniumEvpAlignmentScore() { 
  }

  public TitaniumEvpAlignmentScore evpAlignmentDispersionScore(Object evpAlignmentDispersionScore) {
    
    this.evpAlignmentDispersionScore = evpAlignmentDispersionScore;
    return this;
  }

   /**
   * Get evpAlignmentDispersionScore
   * @return evpAlignmentDispersionScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getEvpAlignmentDispersionScore() {
    return evpAlignmentDispersionScore;
  }


  public void setEvpAlignmentDispersionScore(Object evpAlignmentDispersionScore) {
    this.evpAlignmentDispersionScore = evpAlignmentDispersionScore;
  }


  public TitaniumEvpAlignmentScore evpMid(Object evpMid) {
    
    this.evpMid = evpMid;
    return this;
  }

   /**
   * Get evpMid
   * @return evpMid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getEvpMid() {
    return evpMid;
  }


  public void setEvpMid(Object evpMid) {
    this.evpMid = evpMid;
  }


  public TitaniumEvpAlignmentScore score(Object score) {
    
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


  public TitaniumEvpAlignmentScore scoreStatus(String scoreStatus) {
    
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


  public TitaniumEvpAlignmentScore submissionMean(Object submissionMean) {
    
    this.submissionMean = submissionMean;
    return this;
  }

   /**
   * Get submissionMean
   * @return submissionMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmissionMean() {
    return submissionMean;
  }


  public void setSubmissionMean(Object submissionMean) {
    this.submissionMean = submissionMean;
  }


  public TitaniumEvpAlignmentScore submissionStdDev(Object submissionStdDev) {
    
    this.submissionStdDev = submissionStdDev;
    return this;
  }

   /**
   * Get submissionStdDev
   * @return submissionStdDev
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmissionStdDev() {
    return submissionStdDev;
  }


  public void setSubmissionStdDev(Object submissionStdDev) {
    this.submissionStdDev = submissionStdDev;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumEvpAlignmentScore titaniumEvpAlignmentScore = (TitaniumEvpAlignmentScore) o;
    return Objects.equals(this.evpAlignmentDispersionScore, titaniumEvpAlignmentScore.evpAlignmentDispersionScore) &&
        Objects.equals(this.evpMid, titaniumEvpAlignmentScore.evpMid) &&
        Objects.equals(this.score, titaniumEvpAlignmentScore.score) &&
        Objects.equals(this.scoreStatus, titaniumEvpAlignmentScore.scoreStatus) &&
        Objects.equals(this.submissionMean, titaniumEvpAlignmentScore.submissionMean) &&
        Objects.equals(this.submissionStdDev, titaniumEvpAlignmentScore.submissionStdDev);
  }

  @Override
  public int hashCode() {
    return Objects.hash(evpAlignmentDispersionScore, evpMid, score, scoreStatus, submissionMean, submissionStdDev);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumEvpAlignmentScore {\n");
    sb.append("    evpAlignmentDispersionScore: ").append(toIndentedString(evpAlignmentDispersionScore)).append("\n");
    sb.append("    evpMid: ").append(toIndentedString(evpMid)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    scoreStatus: ").append(toIndentedString(scoreStatus)).append("\n");
    sb.append("    submissionMean: ").append(toIndentedString(submissionMean)).append("\n");
    sb.append("    submissionStdDev: ").append(toIndentedString(submissionStdDev)).append("\n");
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
    openapiFields.add("evpAlignmentDispersionScore");
    openapiFields.add("evpMid");
    openapiFields.add("score");
    openapiFields.add("scoreStatus");
    openapiFields.add("submissionMean");
    openapiFields.add("submissionStdDev");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumEvpAlignmentScore
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumEvpAlignmentScore.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumEvpAlignmentScore is not found in the empty JSON string", TitaniumEvpAlignmentScore.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumEvpAlignmentScore.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumEvpAlignmentScore` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("scoreStatus") != null && !jsonObj.get("scoreStatus").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `scoreStatus` to be a primitive type in the JSON string but got `%s`", jsonObj.get("scoreStatus").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumEvpAlignmentScore.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumEvpAlignmentScore' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumEvpAlignmentScore> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumEvpAlignmentScore.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumEvpAlignmentScore>() {
           @Override
           public void write(JsonWriter out, TitaniumEvpAlignmentScore value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumEvpAlignmentScore read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumEvpAlignmentScore given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumEvpAlignmentScore
  * @throws IOException if the JSON string is invalid with respect to TitaniumEvpAlignmentScore
  */
  public static TitaniumEvpAlignmentScore fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumEvpAlignmentScore.class);
  }

 /**
  * Convert an instance of TitaniumEvpAlignmentScore to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}


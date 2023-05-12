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
 * TitaniumExpertiseScore
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-12T16:18:26.451720Z[UTC]")
public class TitaniumExpertiseScore {
  public static final String SERIALIZED_NAME_CHALLENGE_SCORE = "challengeScore";
  @SerializedName(SERIALIZED_NAME_CHALLENGE_SCORE)
  private Object challengeScore;

  public static final String SERIALIZED_NAME_CONSENSUS_DISTANCE_SCORE = "consensusDistanceScore";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_DISTANCE_SCORE)
  private Object consensusDistanceScore;

  public static final String SERIALIZED_NAME_CONSENSUS_SCORE = "consensusScore";
  @SerializedName(SERIALIZED_NAME_CONSENSUS_SCORE)
  private Object consensusScore;

  public static final String SERIALIZED_NAME_DIMENSION_CREDIT_SCORE = "dimensionCreditScore";
  @SerializedName(SERIALIZED_NAME_DIMENSION_CREDIT_SCORE)
  private Object dimensionCreditScore;

  public static final String SERIALIZED_NAME_EXPERTISE_RANK = "expertiseRank";
  @SerializedName(SERIALIZED_NAME_EXPERTISE_RANK)
  private Object expertiseRank;

  public static final String SERIALIZED_NAME_EXPERTS_COUNT = "expertsCount";
  @SerializedName(SERIALIZED_NAME_EXPERTS_COUNT)
  private Object expertsCount;

  public static final String SERIALIZED_NAME_PROXIMITY_TO_POST_CHALLENGE_CONSENSUS_MEAN = "proximityToPostChallengeConsensusMean";
  @SerializedName(SERIALIZED_NAME_PROXIMITY_TO_POST_CHALLENGE_CONSENSUS_MEAN)
  private Object proximityToPostChallengeConsensusMean;

  public static final String SERIALIZED_NAME_SCORE = "score";
  @SerializedName(SERIALIZED_NAME_SCORE)
  private Object score;

  public static final String SERIALIZED_NAME_SUBMITTED_SCORE = "submittedScore";
  @SerializedName(SERIALIZED_NAME_SUBMITTED_SCORE)
  private Object submittedScore;

  public TitaniumExpertiseScore() { 
  }

  public TitaniumExpertiseScore challengeScore(Object challengeScore) {
    
    this.challengeScore = challengeScore;
    return this;
  }

   /**
   * Get challengeScore
   * @return challengeScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getChallengeScore() {
    return challengeScore;
  }


  public void setChallengeScore(Object challengeScore) {
    this.challengeScore = challengeScore;
  }


  public TitaniumExpertiseScore consensusDistanceScore(Object consensusDistanceScore) {
    
    this.consensusDistanceScore = consensusDistanceScore;
    return this;
  }

   /**
   * Get consensusDistanceScore
   * @return consensusDistanceScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsensusDistanceScore() {
    return consensusDistanceScore;
  }


  public void setConsensusDistanceScore(Object consensusDistanceScore) {
    this.consensusDistanceScore = consensusDistanceScore;
  }


  public TitaniumExpertiseScore consensusScore(Object consensusScore) {
    
    this.consensusScore = consensusScore;
    return this;
  }

   /**
   * Get consensusScore
   * @return consensusScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getConsensusScore() {
    return consensusScore;
  }


  public void setConsensusScore(Object consensusScore) {
    this.consensusScore = consensusScore;
  }


  public TitaniumExpertiseScore dimensionCreditScore(Object dimensionCreditScore) {
    
    this.dimensionCreditScore = dimensionCreditScore;
    return this;
  }

   /**
   * Get dimensionCreditScore
   * @return dimensionCreditScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getDimensionCreditScore() {
    return dimensionCreditScore;
  }


  public void setDimensionCreditScore(Object dimensionCreditScore) {
    this.dimensionCreditScore = dimensionCreditScore;
  }


  public TitaniumExpertiseScore expertiseRank(Object expertiseRank) {
    
    this.expertiseRank = expertiseRank;
    return this;
  }

   /**
   * Get expertiseRank
   * @return expertiseRank
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getExpertiseRank() {
    return expertiseRank;
  }


  public void setExpertiseRank(Object expertiseRank) {
    this.expertiseRank = expertiseRank;
  }


  public TitaniumExpertiseScore expertsCount(Object expertsCount) {
    
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


  public TitaniumExpertiseScore proximityToPostChallengeConsensusMean(Object proximityToPostChallengeConsensusMean) {
    
    this.proximityToPostChallengeConsensusMean = proximityToPostChallengeConsensusMean;
    return this;
  }

   /**
   * Get proximityToPostChallengeConsensusMean
   * @return proximityToPostChallengeConsensusMean
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getProximityToPostChallengeConsensusMean() {
    return proximityToPostChallengeConsensusMean;
  }


  public void setProximityToPostChallengeConsensusMean(Object proximityToPostChallengeConsensusMean) {
    this.proximityToPostChallengeConsensusMean = proximityToPostChallengeConsensusMean;
  }


  public TitaniumExpertiseScore score(Object score) {
    
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


  public TitaniumExpertiseScore submittedScore(Object submittedScore) {
    
    this.submittedScore = submittedScore;
    return this;
  }

   /**
   * Get submittedScore
   * @return submittedScore
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Object getSubmittedScore() {
    return submittedScore;
  }


  public void setSubmittedScore(Object submittedScore) {
    this.submittedScore = submittedScore;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumExpertiseScore titaniumExpertiseScore = (TitaniumExpertiseScore) o;
    return Objects.equals(this.challengeScore, titaniumExpertiseScore.challengeScore) &&
        Objects.equals(this.consensusDistanceScore, titaniumExpertiseScore.consensusDistanceScore) &&
        Objects.equals(this.consensusScore, titaniumExpertiseScore.consensusScore) &&
        Objects.equals(this.dimensionCreditScore, titaniumExpertiseScore.dimensionCreditScore) &&
        Objects.equals(this.expertiseRank, titaniumExpertiseScore.expertiseRank) &&
        Objects.equals(this.expertsCount, titaniumExpertiseScore.expertsCount) &&
        Objects.equals(this.proximityToPostChallengeConsensusMean, titaniumExpertiseScore.proximityToPostChallengeConsensusMean) &&
        Objects.equals(this.score, titaniumExpertiseScore.score) &&
        Objects.equals(this.submittedScore, titaniumExpertiseScore.submittedScore);
  }

  @Override
  public int hashCode() {
    return Objects.hash(challengeScore, consensusDistanceScore, consensusScore, dimensionCreditScore, expertiseRank, expertsCount, proximityToPostChallengeConsensusMean, score, submittedScore);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumExpertiseScore {\n");
    sb.append("    challengeScore: ").append(toIndentedString(challengeScore)).append("\n");
    sb.append("    consensusDistanceScore: ").append(toIndentedString(consensusDistanceScore)).append("\n");
    sb.append("    consensusScore: ").append(toIndentedString(consensusScore)).append("\n");
    sb.append("    dimensionCreditScore: ").append(toIndentedString(dimensionCreditScore)).append("\n");
    sb.append("    expertiseRank: ").append(toIndentedString(expertiseRank)).append("\n");
    sb.append("    expertsCount: ").append(toIndentedString(expertsCount)).append("\n");
    sb.append("    proximityToPostChallengeConsensusMean: ").append(toIndentedString(proximityToPostChallengeConsensusMean)).append("\n");
    sb.append("    score: ").append(toIndentedString(score)).append("\n");
    sb.append("    submittedScore: ").append(toIndentedString(submittedScore)).append("\n");
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
    openapiFields.add("challengeScore");
    openapiFields.add("consensusDistanceScore");
    openapiFields.add("consensusScore");
    openapiFields.add("dimensionCreditScore");
    openapiFields.add("expertiseRank");
    openapiFields.add("expertsCount");
    openapiFields.add("proximityToPostChallengeConsensusMean");
    openapiFields.add("score");
    openapiFields.add("submittedScore");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumExpertiseScore
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumExpertiseScore.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumExpertiseScore is not found in the empty JSON string", TitaniumExpertiseScore.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumExpertiseScore.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumExpertiseScore` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumExpertiseScore.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumExpertiseScore' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumExpertiseScore> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumExpertiseScore.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumExpertiseScore>() {
           @Override
           public void write(JsonWriter out, TitaniumExpertiseScore value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumExpertiseScore read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumExpertiseScore given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumExpertiseScore
  * @throws IOException if the JSON string is invalid with respect to TitaniumExpertiseScore
  */
  public static TitaniumExpertiseScore fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumExpertiseScore.class);
  }

 /**
  * Convert an instance of TitaniumExpertiseScore to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}


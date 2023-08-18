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
import java.math.BigDecimal;

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
 * TitaniumSubmissionEvidenceAnchorDetails
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-18T15:38:23.771664Z[UTC]")
public class TitaniumSubmissionEvidenceAnchorDetails {
  public static final String SERIALIZED_NAME_DISTANCE_TO_CONSENSUS = "distanceToConsensus";
  @SerializedName(SERIALIZED_NAME_DISTANCE_TO_CONSENSUS)
  private BigDecimal distanceToConsensus;

  public static final String SERIALIZED_NAME_SUBMISSION_EVIDENCE = "submissionEvidence";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_EVIDENCE)
  private BigDecimal submissionEvidence;

  public TitaniumSubmissionEvidenceAnchorDetails() { 
  }

  public TitaniumSubmissionEvidenceAnchorDetails distanceToConsensus(BigDecimal distanceToConsensus) {
    
    this.distanceToConsensus = distanceToConsensus;
    return this;
  }

   /**
   * Get distanceToConsensus
   * @return distanceToConsensus
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getDistanceToConsensus() {
    return distanceToConsensus;
  }


  public void setDistanceToConsensus(BigDecimal distanceToConsensus) {
    this.distanceToConsensus = distanceToConsensus;
  }


  public TitaniumSubmissionEvidenceAnchorDetails submissionEvidence(BigDecimal submissionEvidence) {
    
    this.submissionEvidence = submissionEvidence;
    return this;
  }

   /**
   * Get submissionEvidence
   * @return submissionEvidence
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getSubmissionEvidence() {
    return submissionEvidence;
  }


  public void setSubmissionEvidence(BigDecimal submissionEvidence) {
    this.submissionEvidence = submissionEvidence;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumSubmissionEvidenceAnchorDetails titaniumSubmissionEvidenceAnchorDetails = (TitaniumSubmissionEvidenceAnchorDetails) o;
    return Objects.equals(this.distanceToConsensus, titaniumSubmissionEvidenceAnchorDetails.distanceToConsensus) &&
        Objects.equals(this.submissionEvidence, titaniumSubmissionEvidenceAnchorDetails.submissionEvidence);
  }

  @Override
  public int hashCode() {
    return Objects.hash(distanceToConsensus, submissionEvidence);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumSubmissionEvidenceAnchorDetails {\n");
    sb.append("    distanceToConsensus: ").append(toIndentedString(distanceToConsensus)).append("\n");
    sb.append("    submissionEvidence: ").append(toIndentedString(submissionEvidence)).append("\n");
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
    openapiFields.add("distanceToConsensus");
    openapiFields.add("submissionEvidence");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumSubmissionEvidenceAnchorDetails
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumSubmissionEvidenceAnchorDetails.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumSubmissionEvidenceAnchorDetails is not found in the empty JSON string", TitaniumSubmissionEvidenceAnchorDetails.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumSubmissionEvidenceAnchorDetails.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumSubmissionEvidenceAnchorDetails` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumSubmissionEvidenceAnchorDetails.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumSubmissionEvidenceAnchorDetails' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumSubmissionEvidenceAnchorDetails> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumSubmissionEvidenceAnchorDetails.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumSubmissionEvidenceAnchorDetails>() {
           @Override
           public void write(JsonWriter out, TitaniumSubmissionEvidenceAnchorDetails value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumSubmissionEvidenceAnchorDetails read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumSubmissionEvidenceAnchorDetails given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumSubmissionEvidenceAnchorDetails
  * @throws IOException if the JSON string is invalid with respect to TitaniumSubmissionEvidenceAnchorDetails
  */
  public static TitaniumSubmissionEvidenceAnchorDetails fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumSubmissionEvidenceAnchorDetails.class);
  }

 /**
  * Convert an instance of TitaniumSubmissionEvidenceAnchorDetails to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

